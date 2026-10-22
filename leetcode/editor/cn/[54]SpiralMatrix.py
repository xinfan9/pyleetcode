class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
#  
#  
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
# 
#  Related Topics 数组 矩阵 模拟 👍 2203 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def next(self, i: int, j: int, m: int, n: int, det: int):
        k = det // 4
        d = det % 4
        if d == 0:
            if j + 1 == n - k:
                det += 1
                i = i + 1
            else:
                j = j + 1
        elif d == 1:
            if i + 1 == m - k:
                det += 1
                j = j - 1
            else:
                i = i + 1
        elif d == 2:
            if j - 1 < 0 + k:
                det += 1
                i = i - 1
            else:
                j = j - 1
        else:
            if i - 1 < 1 + k:
                det += 1
                j = j + 1
            else:
                i = i - 1
        return i, j, det
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        i, j = 0, 0
        m, n = len(matrix), len(matrix[0])
        cnt = 0
        det = 0
        res = []
        while cnt < m*n:
            res.append(matrix[i][j])
            i, j, det = self.next(i, j, m, n, det)
            cnt += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
