class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。 
# 
#  整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2 。 
# 
#  返回被除数 dividend 除以除数 divisor 得到的 商 。 
# 
#  注意：假设我们的环境只能存储 32 位 有符号整数，其数值范围是 [−2³¹, 231 − 1] 。本题中，如果商 严格大于 231 − 1 ，则返回 2
# 31 − 1 ；如果商 严格小于 -2³¹ ，则返回 -2³¹ 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = 3.33333.. ，向零截断后得到 3 。 
# 
#  示例 2: 
# 
#  
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = -2.33333.. ，向零截断后得到 -2 。 
# 
#  
# 
#  提示： 
# 
#  
#  -2³¹ <= dividend, divisor <= 2³¹ - 1 
#  divisor != 0 
#  
# 
#  Related Topics 位运算 数学 👍 1356 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        negative = (dividend > 0) != (divisor > 0)
        a = -dividend if dividend > 0 else dividend
        b = -divisor if divisor > 0 else divisor

        result = 0
        while a <= b:
            value = b
            count = 1
            while value >= INT_MIN - value and a <= value + value:
                value += value
                count += count
            a -= value
            result += count
        return -result if negative else result
# leetcode submit region end(Prohibit modification and deletion)
