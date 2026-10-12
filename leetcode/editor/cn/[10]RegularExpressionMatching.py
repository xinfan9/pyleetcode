class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。 
# 
#  
#  '.' 匹配任意单个字符 
#  '*' 匹配零个或多个前面的那一个元素 
#  
# 
#  返回一个布尔值，表示匹配是否覆盖整个输入字符串（而非部分）。 
# 
#  示例 1： 
# 
#  
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#  
# 
#  示例 2: 
# 
#  
# 输入：s = "aa", p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "ab", p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 20 
#  1 <= p.length <= 20 
#  s 只包含从 a-z 的小写字母。 
#  p 只包含从 a-z 的小写字母，以及字符 . 和 *。 
#  保证每次出现字符 * 时，前面都匹配到有效的字符 
#  
# 
#  Related Topics 递归 字符串 动态规划 👍 4240 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        # dp[i][j] 表示 s[:i] 与 p[:j] 是否匹配
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True  # 空串匹配空模式

        # 初始化：空串 vs 模式，x* 可以匹配零个字符
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # 情况一：x* 匹配零次，跳过 x*
                    dp[i][j] = dp[i][j - 2]
                    # 情况二：x* 匹配一次或多次，前一个字符能配 s[i-1]
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # 普通字符或 '.' 直接匹配单个字符
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]

# leetcode submit region end(Prohibit modification and deletion)
