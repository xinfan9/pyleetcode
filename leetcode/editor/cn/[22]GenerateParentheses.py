class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：["()"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
# 
#  Related Topics 字符串 动态规划 回溯 括号序列 👍 4170 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
left = 0
right = 0
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        cur_str = []
        def backtrace(i):
            global left
            global right
            if i == 2*n:
                res.append(''.join(cur_str))
                return
            if left < n:
                cur_str.append('(')
                left += 1
                backtrace(i + 1)
                cur_str.pop()
                left -= 1
            if left > right:
                cur_str.append(')')
                right += 1
                backtrace(i + 1)
                cur_str.pop()
                right -= 1

        backtrace(0)
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
