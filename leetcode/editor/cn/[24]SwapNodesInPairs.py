class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 100] 内 
#  0 <= Node.val <= 100 
#  
# 
#  Related Topics 递归 链表 👍 2683 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = ListNode(next=head)
        begin = node
        while begin:
            end = begin
            for i in range(2):
                end = end.next
                if not end:
                    return node.next
            next = end.next
            end.next = None
            begin.next, tail = self.reverse(begin.next)
            tail.next = next
            begin = tail
        return node.next

    def reverse(self, head):
        node = ListNode()
        next = None
        tail = head
        while head:
            node.next = head
            head = head.next
            node.next.next = next
            next = node.next
        return node.next, tail

# leetcode submit region end(Prohibit modification and deletion)
