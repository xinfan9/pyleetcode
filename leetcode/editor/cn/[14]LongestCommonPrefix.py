from functools import cmp_to_key


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#  
# 
#  示例 2： 
# 
#  
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] 如果非空，则仅由小写英文字母组成 
#  
# 
#  Related Topics 字典树 数组 字符串 👍 3551 👎 0

# leetcode submit region begin(Prohibit modification and deletion)
def cmp(a, b):
    # • 如果 a < b：返回 负数（通常是 -1）
    # • 如果 a == b：返回 0
    # • 如果 a > b：返回 正数（通常是 1）
    return len(a) - len(b)

# 还可以写为 strs.sorted(key=lambda x: len(x)) , python 3：排序时关注的是“元素的核心权重/特征是什么”
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort(key=lambda x: len(x))
        target = strs[0]
        res = []
        for i, c in enumerate(target):
            for s in strs[1:]:
                if s[i] != c:
                    return "".join(res)
            res.append(c)
        return "".join(res)
# leetcode submit region end(Prohibit modification and deletion)
