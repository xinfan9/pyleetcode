
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。 
# 
#  如果反转后整数超过 32 位的有符号整数的范围 [−2³¹, 231 − 1] ，就返回 0。 
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 123
# 输出：321
#  
# 
#  示例 2： 
# 
#  
# 输入：x = -123
# 输出：-321
#  
# 
#  示例 3： 
# 
#  
# 输入：x = 120
# 输出：21
#  
# 
#  示例 4： 
# 
#  
# 输入：x = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  -2³¹ <= x <= 2³¹ - 1 
#  
# 
#  Related Topics 数学 👍 4197 👎 0

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        a = 1
        if x < 0:
            a = -1
            x = -x

        i32_max = pow(2, 31) - 1
        i32_min = -pow(2, 31)
        res = 0
        while x != 0:
            if (a > 0 and res > i32_max/10) or (a < 0 and res > -i32_min/10):
                return 0
            cur = x % 10
            x = x // 10
            res = res*10 + cur
        return res*a
        
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()