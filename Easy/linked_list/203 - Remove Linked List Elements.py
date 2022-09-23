#Method 1:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if head is None:
            return None
        
        if head.next is None:
            if head.val == val:
                return None
            else:
                return head
        
        curr = head
        
        while curr is not None:
            
            while curr:
                if curr.next is not None:
                    if curr.next.val == val:
                        curr.next = curr.next.next
                    else:
                        break
                else:
                    break
            if curr.val == val:
                if curr.next is None:
                    return None
                head = curr.next
                curr=head
            else:
                curr = curr.next
                
        return head
