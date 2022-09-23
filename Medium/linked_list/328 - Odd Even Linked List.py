#Method 1:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return None
        
        odd = head
        estart = head.next
        even = head.next
        
        while even and even.next:
            
            odd.next= odd.next.next
            odd=odd.next
            even.next= even.next.next
            even=even.next
        
        odd.next = estart
        return head

