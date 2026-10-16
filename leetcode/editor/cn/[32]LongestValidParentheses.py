class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。 
# 
#  左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"。 
# 
#  
# 
#  
#  
#  示例 1： 
#  
#  
# 
#  
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = ""
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 3 * 10⁴ 
#  s[i] 为 '(' 或 ')' 
#  
# 
#  Related Topics 栈 字符串 动态规划 括号序列 👍 2950 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        res = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res
# leetcode submit region end(Prohibit modification and deletion)
