class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置在下标 0。 
# 
#  每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在索引 i 处，你可以跳转到任意 (i + j) 处： 
# 
#  
#  0 <= j <= nums[i] 且 
#  i + j < n 
#  
# 
#  返回到达 n - 1 的最小跳跃次数。测试用例保证可以到达 n - 1。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [2,3,0,1,4]
# 输出: 2
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  0 <= nums[i] <= 1000 
#  题目保证可以到达 n - 1 
#  
# 
#  Related Topics 贪心 数组 动态规划 👍 3114 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def jump(self, nums: list[int]) -> int:
    #     n = len(nums)
    #     jumps, cur_end, farthest = 0, 0, 0
    #     for i in range(n - 1):
    #         farthest = max(farthest, i + nums[i])
    #         if i == cur_end:      # 走到当前边界，必须再跳一步
    #             jumps += 1
    #             cur_end = farthest
    #     return jumps
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [(2**31 - 1) for _ in nums ]
        dp[0] = 0
        for i, num in enumerate(nums):
            if dp[i] == 2**31 - 1:
                continue
            for j in range(i + 1, min(i + num, n - 1) + 1):
                dp[j] = min(dp[i] + 1, dp[j])
        return dp[n - 1]
# leetcode submit region end(Prohibit modification and deletion)
