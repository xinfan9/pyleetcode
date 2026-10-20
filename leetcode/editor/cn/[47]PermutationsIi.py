class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
# 
#  Related Topics 数组 回溯 排序 👍 1823 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []
        my_set = set()
        target = []
        nums.sort()
        def backtrace(i:int):
            if i == n:
                res.append(target[:])
                return
            for j, num in enumerate(nums):
                if j in my_set:
                    continue
                if j > 0 and nums[j - 1] == num and (j-1) not in my_set:
                    continue
                my_set.add(j)
                target.append(num)
                backtrace(i + 1)
                my_set.remove(j)
                target.pop()
        backtrace(0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
