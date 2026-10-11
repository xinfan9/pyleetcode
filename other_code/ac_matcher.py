"""Aho-Corasick 多模式串匹配自动机。

给定一组模式串 P1..Pk 和文本 T，一次扫描找出所有模式串在 T 中的所有出现。
总模式串长度 m，文本长度 n，命中总数 z：
- 构建 O(m)（最坏 O(m·σ)，σ 为字符集大小）
- 匹配 O(n + z)

核心三件套：
1. Trie：把全部模式串建成字典树，每个节点一个状态
2. fail 链接：失配时跳到"当前已匹配后缀的最长模式串前缀"对应的状态
3. 字典后缀链接 dict：沿 fail 链上最近的"有模式串结束"的状态，
   用来在一次失配跳转后不回溯地报告全部命中
"""

from collections import deque


class AhoCorasick:
    def __init__(self):
        self.next = [{}]      # next[state][char] -> 下一个状态（Trie 转移）
        self.fail = [0]       # fail[state] -> 失配跳转目标
        self.out = [set()]    # 在该状态结束的模式串编号集合
        self.dict = [-1]      # 字典后缀链接；-1 表示没有
        self.patterns = []    # 模式串列表，编号即下标
        self._built = False

    # ---------- 构建 ----------

    def add_pattern(self, pattern: str) -> int:
        """加入一个模式串，返回其编号。空串不允许。"""
        if not pattern:
            raise ValueError('模式串不能为空')
        pid = len(self.patterns)
        self.patterns.append(pattern)

        s = 0
        for ch in pattern:
            if ch not in self.next[s]:
                self.next[s][ch] = len(self.next)
                self.next.append({})
                self.fail.append(0)
                self.out.append(set())
                self.dict.append(-1)
            s = self.next[s][ch]
        self.out[s].add(pid)
        return pid

    def build(self):
        """按 BFS 顺序计算所有节点的 fail 和 dict 链接。"""
        if self._built:
            return
        queue = deque()
        # 根的直接孩子：fail 指向根（初始值就是 0），dict 为 -1（根无输出）
        for ch, s in self.next[0].items():
            queue.append(s)

        while queue:
            v = queue.popleft()
            for ch, u in self.next[v].items():
                queue.append(u)
                # 找失配目标：从 fail[父] 开始，沿 fail 链找有 ch 转移的状态
                f = self.fail[v]
                while f and ch not in self.next[f]:
                    f = self.fail[f]
                self.fail[u] = self.next[f].get(ch, 0)
                # 字典后缀链接：fail[u] 若有输出就用它，否则沿用它的 dict
                d = self.fail[u]
                self.dict[u] = d if self.out[d] else self.dict[d]
        self._built = True

    # ---------- 匹配 ----------

    def search(self, text: str):
        """返回所有命中 [(结束下标, 模式串编号), ...]。"""
        if not self._built:
            self.build()
        matches = []
        s = 0
        for i, ch in enumerate(text):
            # 失配则沿 fail 链跳转
            while s and ch not in self.next[s]:
                s = self.fail[s]
            s = self.next[s].get(ch, 0)
            # 报告当前状态及其字典后缀链上所有命中
            t = s
            while t != -1:
                for pid in self.out[t]:
                    matches.append((i, pid))
                t = self.dict[t]
        return matches

    def count(self, text: str):
        """返回每个模式串在 text 中的出现次数。"""
        res = [0] * len(self.patterns)
        for _, pid in self.search(text):
            res[pid] += 1
        return res

    def find_all(self, text: str):
        """返回 [(起始下标, 结束下标, 模式串), ...]。"""
        return [
            (i - len(self.patterns[pid]) + 1, i, self.patterns[pid])
            for i, pid in self.search(text)
        ]

    def contains(self, text: str) -> bool:
        """任意模式串是否出现（可提前退出，比 search 更快）。"""
        if not self._built:
            self.build()
        s = 0
        for ch in text:
            while s and ch not in self.next[s]:
                s = self.fail[s]
            s = self.next[s].get(ch, 0)
            if self.out[s] or self.dict[s] != -1:
                return True
        return False

"""AC 匹配器（AhoCorasick）测试用例。

直接运行（无需 pytest）：
    python3 test_ac_matcher.py

约定：
    - 每个 test_* 函数是一个用例，断言失败即用例失败；
    - 全部通过时退出码为 0，有失败时退出码为 1，可接入 CI；
    - 随机用例固定种子，结果可复现。
"""

import random

# ---------- 朴素参考实现（用于对拍） ----------

def naive_find_all(text: str, pat: str) -> list[int]:
    """返回 pat 在 text 中的所有起始下标（允许重叠）。"""
    pos, start = [], 0
    while True:
        i = text.find(pat, start)
        if i == -1:
            break
        pos.append(i)
        start = i + 1
    return pos


# ---------- 用例 ----------

def test_empty_text_no_match():
    """空文本：任何模式串都不命中。"""
    ac = AhoCorasick()
    ac.add_pattern('abc')
    ac.add_pattern('a')
    ac.build()
    assert ac.search('') == []
    assert ac.find_all('') == []
    assert ac.count('') == [0, 0]
    assert ac.contains('') is False


def test_empty_pattern_rejected():
    """空模式串必须报错。"""
    ac = AhoCorasick()
    try:
        ac.add_pattern('')
    except ValueError:
        pass
    else:
        raise AssertionError('空模式串应该抛出 ValueError')


def test_no_match():
    """文本不含任何模式串。"""
    ac = AhoCorasick()
    for p in ['abc', 'xyz', 'hello']:
        ac.add_pattern(p)
    ac.build()
    assert ac.search('nothing here') == []
    assert ac.contains('nothing here') is False


def test_single_character():
    """单字符模式串。"""
    ac = AhoCorasick()
    ac.add_pattern('a')
    ac.build()
    text = 'banana'
    assert [(i - 0, 0) for i, _ in ac.search(text)] == [(i, 0) for i in (1, 3, 5)]
    assert ac.count(text) == [3]
    assert ac.contains(text) is True


def test_classic_ushers():
    """经典例子：he / she / his / hers 匹配 ushers。"""
    ac = AhoCorasick()
    for p in ['he', 'she', 'his', 'hers']:
        ac.add_pattern(p)
    ac.build()
    text = 'ushers'
    assert ac.find_all(text) == [(1, 3, 'she'), (2, 3, 'he'), (2, 5, 'hers')]
    assert ac.count(text) == [1, 1, 0, 1]
    assert ac.contains(text) is True


def test_overlapping_matches():
    """模式串互相重叠：a / aa / aaa 在 a*8 上。"""
    ac = AhoCorasick()
    for p in ['a', 'aa', 'aaa']:
        ac.add_pattern(p)
    ac.build()
    text = 'a' * 8
    assert ac.count(text) == [8, 7, 6]


def test_share_suffix_dict_link():
    """一个模式串是另一个的后缀：he 是 she 的后缀，靠 dict 链接命中。"""
    ac = AhoCorasick()
    ac.add_pattern('he')
    ac.add_pattern('she')
    ac.build()
    assert sorted(ac.find_all('she')) == sorted([(0, 2, 'she'), (1, 2, 'he')])


def test_share_prefix():
    """模式串互为前缀：he / her / hers。"""
    ac = AhoCorasick()
    for p in ['he', 'her', 'hers']:
        ac.add_pattern(p)
    ac.build()
    text = 'hers'
    assert sorted(ac.find_all(text)) == sorted([
        (0, 3, 'hers'),
        (0, 2, 'her'),
        (0, 1, 'he'),
    ])
    assert ac.count(text) == [1, 1, 1]


def test_multiple_matches_same_end():
    """同一结束位置命中多个模式串：ab 和 b 都结束于下标 1。"""
    ac = AhoCorasick()
    ac.add_pattern('ab')
    ac.add_pattern('b')
    ac.build()
    assert sorted(ac.search('ab')) == sorted([(1, 0), (1, 1)])


def test_unicode():
    """Unicode 文本（中文）。"""
    ac = AhoCorasick()
    ac.add_pattern('违禁词')
    ac.add_pattern('违规')
    ac.build()
    text = '本条消息包含违禁词和违规内容'
    assert ac.contains(text) is True
    assert ac.count(text) == [1, 1]
    assert ac.find_all(text) == [(6, 8, '违禁词'), (10, 11, '违规')]


def test_auto_build():
    """不显式调用 build()，首次使用自动构建。"""
    ac = AhoCorasick()
    ac.add_pattern('abc')
    assert ac.search('xxabc') == [(4, 0)]   # 'abc' 结束于下标 4
    assert ac.contains('abc') is True


def test_add_after_build_rebuilds():
    """build() 之后再加模式串，下次使用自动重建。"""
    ac = AhoCorasick()
    ac.add_pattern('ab')
    ac.build()
    assert ac.contains('ab') is True
    ac.add_pattern('cd')            # 构建后新增
    assert ac.contains('cd') is True
    assert ac.contains('ab') is True
    assert ac.contains('xy') is False   # 无命中


def test_build_idempotent():
    """build() 可重复调用，结果不变。"""
    ac = AhoCorasick()
    for p in ['a', 'ab', 'abc']:
        ac.add_pattern(p)
    ac.build()
    ac.build()
    assert ac.count('ababc') == [2, 2, 1]   # a×2, ab×2, abc×1


def test_count_findall_contains_consistent():
    """count / find_all / contains / search 四种入口结果互相一致。"""
    ac = AhoCorasick()
    for p in ['ab', 'bc', 'abc', 'b']:
        ac.add_pattern(p)
    ac.build()
    text = 'abcabc'
    matches = ac.search(text)
    starts = [(i - len(ac.patterns[pid]) + 1, pid) for i, pid in matches]
    fa = ac.find_all(text)
    assert sorted((s, s + len(ac.patterns[pid]) - 1, ac.patterns[pid]) for s, pid in starts) == sorted(fa)
    assert ac.count(text) == [len(naive_find_all(text, p)) for p in ac.patterns]
    assert ac.contains(text) is (len(matches) > 0)


def test_randomized_differential():
    """随机对拍：300 组随机模式集 + 随机文本，与朴素匹配逐位置一致。"""
    random.seed(42)
    alpha = 'abcd'
    for rnd in range(300):
        npat = random.randint(1, 12)
        pats = [
            ''.join(random.choice(alpha) for _ in range(random.randint(1, 8)))
            for _ in range(npat)
        ]
        text = ''.join(random.choice(alpha) for _ in range(random.randint(0, 300)))

        ac = AhoCorasick()
        for p in pats:
            ac.add_pattern(p)

        got = sorted((i - len(pats[pid]) + 1, pid) for i, pid in ac.search(text))
        expected = sorted(
            (s, pid)
            for pid, p in enumerate(pats)
            for s in naive_find_all(text, p)
        )
        assert got == expected, f'第 {rnd} 轮不一致: text={text!r} pats={pats}'


def test_large_corpus():
    """较大规模：200 个模式串、5000 字符文本，与朴素实现结果一致。"""
    random.seed(1)
    alpha = 'abcdefghij'
    pats = [
        ''.join(random.choice(alpha) for _ in range(random.randint(2, 10)))
        for _ in range(200)
    ]
    text = ''.join(random.choice(alpha) for _ in range(5000))

    ac = AhoCorasick()
    for p in pats:
        ac.add_pattern(p)
    ac.build()

    counts = ac.count(text)
    for pid, p in enumerate(pats):
        assert counts[pid] == len(naive_find_all(text, p)), f'模式串 {p!r} 计数不一致'


# ---------- 运行入口 ----------

def _run_all() -> int:
    tests = [
        (name, fn) for name, fn in sorted(globals().items())
        if name.startswith('test_') and callable(fn)
    ]
    passed = failed = 0
    for name, fn in tests:
        try:
            fn()
        except AssertionError as e:
            failed += 1
            print(f'[FAIL] {name}: {e}')
        except Exception as e:  # noqa: BLE001 - 测试入口要兜住所有异常
            failed += 1
            print(f'[ERROR] {name}: {type(e).__name__}: {e}')
        else:
            passed += 1
            print(f'[PASS] {name}')

    print(f'\n共 {len(tests)} 个用例：通过 {passed}，失败 {failed}')
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    raise SystemExit(_run_all())

