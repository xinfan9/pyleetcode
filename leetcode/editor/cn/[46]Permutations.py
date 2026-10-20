class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  nums 中的所有整数 互不相同 
#  
# 
#  Related Topics 数组 回溯 👍 3392 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []
        my_set = set()
        target = []
        def backtrace(i:int):
            if i == n:
                res.append(target[:])
                return
            for num in nums:
                if num in my_set:
                    continue
                my_set.add(num)
                target.append(num)
                backtrace(i + 1)
                my_set.remove(num)
                target.pop()
        backtrace(0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
