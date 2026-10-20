class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
#  
# 
#  示例 2： 
# 
#  
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == height.length 
#  1 <= n <= 2 * 10⁴ 
#  0 <= height[i] <= 10⁵ 
#  
# 
#  Related Topics 栈 数组 双指针 动态规划 单调栈 👍 6463 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: list[int]) -> int:
        # 每个位置可以接的水，等于左右最高的柱子相对矮的那个与自己的差
        n = len(height)
        if n <= 2:
            return 0
        left = [0 for _ in range(n)]
        right = left[:]
        left[0] = height[0]
        right[-1] = height[-1]
        for i in range(1, n):
            left[i] = max(height[i], left[i - 1])

        for i in range(n - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])
        res = 0
        for i in range(0, n):
            h = min(left[i], right[i])
            res += (h - height[i])

        return res

# leetcode submit region end(Prohibit modification and deletion)
