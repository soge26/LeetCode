#Method 1:

# Definition for singly-linked list.
#class ListNode(object):
#     def __init__(self, x):
#            self.val = x
#            self.next = None

class Solution(object):
    
    def hasCycle(self, head):
        """
            :type head: ListNode
            :rtype: bool
            """
        
        """frunner = head.next
            srunner = head
            
            while srunner is not frunner:
            frunner = frunner.next.next
            srunner = srunner.next
            
            return True
            """
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


