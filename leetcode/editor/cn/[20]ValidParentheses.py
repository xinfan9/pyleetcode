class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  每个右括号都有一个对应的相同类型的左括号。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
#  输入：s = "()" 
#  
# 
#  输出：true 
# 
#  示例 2： 
# 
#  
#  输入：s = "()[]{}" 
#  
# 
#  输出：true 
# 
#  示例 3： 
# 
#  
#  输入：s = "(]" 
#  
# 
#  输出：false 
# 
#  示例 4： 
# 
#  
#  输入：s = "([])" 
#  
# 
#  输出：true 
# 
#  示例 5： 
# 
#  
#  输入：s = "([)]" 
#  
# 
#  输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 仅由括号 '()[]{}' 组成 
#  
# 
#  Related Topics 栈 字符串 括号序列 👍 5052 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        table = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for c in s:
            if c in table:
                need = table[c]
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if need != top:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
# leetcode submit region end(Prohibit modification and deletion)
