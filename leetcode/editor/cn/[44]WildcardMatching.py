class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 
#  给你一个输入字符串 (
#  s) 和一个字符模式 (
#  p) ，请你实现一个支持 
#  '?' 和 
#  '*' 匹配规则的通配符匹配：
#  
# 
#  
#  '?' 可以匹配任何单个字符。 
#  '*' 可以匹配任意字符序列（包括空字符序列）。 
#  
# 
#  
#  
#  判定匹配成功的充要条件是：字符模式必须能够 完全匹配 输入字符串（而不是部分匹配）。 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "aa", p = "*"
# 输出：true
# 解释：'*' 可以匹配任意字符串。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "cb", p = "?a"
# 输出：false
# 解释：'?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length, p.length <= 2000 
#  s 仅由小写英文字母组成 
#  p 仅由小写英文字母、'?' 或 '*' 组成 
#  
# 
#  Related Topics 贪心 递归 字符串 动态规划 👍 1274 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] 表示 s[:i] 和 s[: p] 匹配
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1) ]

        dp[0][0] = True
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == '*'

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]
# leetcode submit region end(Prohibit modification and deletion)
