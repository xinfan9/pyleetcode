class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xⁿ ）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
#  
# 
#  示例 2： 
# 
#  
# 输入：x = 2.10000, n = 3
# 输出：9.26100
#  
# 
#  示例 3： 
# 
#  
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25
#  
# 
#  
# 
#  提示： 
# 
#  
#  -100.0 < x < 100.0 
#  -231 <= n <= 231-1 
#  n 是一个整数 
#  要么 x 不为零，要么 n > 0 。 
#  -104 <= xⁿ <= 104 
#  
# 
#  Related Topics 递归 数学 👍 1561 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N: int):
            if N == 0:
                return 1.0
            y = quickMul(N//2)
            return y*y if N % 2 == 0 else y*y*x

        return quickMul(n) if n >= 0 else 1.0/ quickMul(-n)

# leetcode submit region end(Prohibit modification and deletion)
