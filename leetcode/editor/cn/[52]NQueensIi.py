class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。 
# 
#  
# 
#  
#  
#  示例 1： 
#  
#  
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
#  
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 9 
#  
# 
#  Related Topics 回溯 X 算法 👍 613 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def is_valid(self, pos: list[int], checkerboard: list[list[str]]) -> bool:
        n = len(checkerboard)
        x, y = pos
        for i in range(x):
            distance = x - i
            if y - distance >= 0 and checkerboard[i][y - distance] == 'Q':
                return False
            if y + distance < n and checkerboard[i][y + distance] == 'Q':
                return False
        return True
    def totalNQueens(self, n: int) -> int:
        checkerboard = [['.']*n for _ in range(n)]
        res = 0
        col_set = set()
        def backtrace(k: int):
            nonlocal res
            if k == n:
                res = res + 1
                return
            for j in range(n):
                if j in col_set:
                    continue
                if not self.is_valid([k, j], checkerboard):
                    continue
                checkerboard[k][j] = 'Q'
                col_set.add(j)
                backtrace(k + 1)
                col_set.remove(j)
                checkerboard[k][j] = '.'
        backtrace(0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
