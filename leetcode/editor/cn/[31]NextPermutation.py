class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 整数数组的一个 排列 就是将其所有成员以序列或线性顺序排列。 
# 
#  
#  例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。 
#  
# 
#  整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就
# 是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。 
# 
#  
#  例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。 
#  类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。 
#  而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。 
#  
# 
#  给你一个整数数组 nums ，找出 nums 的下一个排列。 
# 
#  必须 原地 修改，只允许使用额外常数空间。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,1]
# 输出：[1,2,3]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,1,5]
# 输出：[1,5,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 100 
#  
# 
#  Related Topics 数组 双指针 👍 2940 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # [1234] [1243]  [123564] [1236456789]
        # 寻找最后一个降序位置起点前一个位置
        descend = -1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                descend = i
        # descend == -1：整体降序，没有下一个排列，重排为最小（升序）
        if descend == -1:
            nums.sort()
            return
        # 在 descend 右侧的降序段里，从右往左找第一个比枢轴 nums[descend-1] 大的数交换
        for j in range(len(nums) - 1, descend - 1, -1):
            if nums[j] > nums[descend - 1]:
                nums[descend - 1], nums[j] = nums[j], nums[descend - 1]
                break
        # 交换后 descend 及其右侧仍为降序，排序成升序
        nums[descend:] = sorted(nums[descend:])

# leetcode submit region end(Prohibit modification and deletion)
