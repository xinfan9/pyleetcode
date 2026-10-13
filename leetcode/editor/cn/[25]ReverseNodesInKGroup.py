class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。 
# 
#  k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
#  
# 
#  
# 提示：
# 
#  
#  链表中的节点数目为 n 
#  1 <= k <= n <= 5000 
#  0 <= Node.val <= 1000 
#  
# 
#  
# 
#  进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？ 
# 
#  
#  
# 
#  Related Topics 递归 链表 👍 2923 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = ListNode(next=head)
        begin = node
        while begin:
            end = begin
            for i in range(k):
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
