from typing import Optional


# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [1, 1000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你可以运用递归和迭代两种方法解决这个问题吗？ 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 3195 👎 0
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = [(root.left, root.right)]      # 镜像对：左子树的左 ↔ 右子树的右
        while stack:
            a, b = stack.pop()
            if not a and not b :
                continue
            if not a or not b or a.val != b.val:
                return False
            stack.append((a.left, b.right))
            stack.append((a.right, b.left))
        return True



# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()