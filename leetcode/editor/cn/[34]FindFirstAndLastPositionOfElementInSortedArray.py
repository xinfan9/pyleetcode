class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。 
# 
#  如果数组中不存在目标值 target，返回 [-1, -1]。 
# 
#  你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1] 
# 
#  示例 3： 
# 
#  
# 输入：nums = [], target = 0
# 输出：[-1,-1] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums 是一个非递减数组 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  Related Topics 数组 二分查找 👍 3325 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def find_left(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2

            print(left, right, mid, nums[mid])
            if nums[mid] == target:
                if mid > 0 and nums[mid - 1] == target:
                    right = mid - 1
                else:
                    return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    def find_right(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                if mid < len(nums) - 1 and nums[mid + 1] == target:
                    left = mid + 1
                else:
                    return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.find_left(nums, target), self.find_right(nums, target)
# leetcode submit region end(Prohibit modification and deletion)
