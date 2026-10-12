class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给定一个长度为 n 的整数数组 nums 和 一个整数 target。 
# 
#  请你从 nums 中选出三个在 不同下标位置 的整数，使它们的和与 target 最接近。 
# 
#  返回这三个数的和。 
# 
#  假定每组输入只存在 恰好 一个解。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,0,0], target = 1
# 输出：0
# 解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。 
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 1000 
#  -1000 <= nums[i] <= 1000 
#  -10⁴ <= target <= 10⁴ 
#  
# 
#  Related Topics 数组 双指针 排序 👍 1827 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = -3001
        gap = float('inf')
        nums.sort()
        for i, num in enumerate(nums[:-2]):
            if i > 0 and nums[i - 1] == num:
                continue
            need_sum = target - num
            left, right = i + 1, len(nums) - 1
            while left < right:
                num2, num3 = nums[left], nums[right]
                sum = num2 + num3
                new_gap = sum - need_sum
                if abs(new_gap) < gap:
                    res = num + num2 + num3
                    gap = abs(new_gap)
                if new_gap < 0:
                    while left < right and nums[left] == num2:
                        left += 1
                if new_gap > 0:
                    while left < right and nums[right] == num3:
                        right -= 1
                if new_gap == 0:
                    return num + num2 + num3

        return res
# leetcode submit region end(Prohibit modification and deletion)
