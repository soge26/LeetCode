#Method 1:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        
        prev = None
        curr=head
        
        while curr is not None:
            next_=curr.next
            curr.next=prev
            prev=curr
            curr= next_

        return prev
