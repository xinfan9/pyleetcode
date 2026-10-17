class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用 一次 。 
# 
#  注意：解集不能包含重复的组合。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ] 
# 
#  示例 2: 
# 
#  
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ] 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
# 
#  Related Topics 数组 回溯 👍 1765 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        tmp = []
        candidates = sorted(candidates)
        # print(candidates)
        def backtrace(n, i):
            if n > target:
                pass
            elif n == target:
                res.append(tmp[:])
            else:
                for j in range(i + 1, len(candidates)):
                    if j > i + 1 and candidates[j] == candidates[j - 1]:
                        continue
                    num = candidates[j]
                    tmp.append(num)
                    n = n + num
                    backtrace(n, j)
                    n = n - num
                    tmp.pop()
        backtrace(0 , -1)

        return res
# leetcode submit region end(Prohibit modification and deletion)
