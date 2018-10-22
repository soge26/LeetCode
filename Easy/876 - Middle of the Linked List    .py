#Method 1:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        f = head
        s = head
        
        while f:
            if f.next is None:
                return s
            elif f.next is not None and f.next.next is None:
                return s.next
            else:
                f = f.next.next
                s = s.next
