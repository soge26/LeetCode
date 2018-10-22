#Method 1:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return None
        
        ind=1
        curr = head
        
        while curr.next is not None:
            curr = curr.next
            ind+=1
    
        index = ind-n        
        curr=head
        i=0
        
        if index == 0:
            head = curr.next
            return head
        else:
            while i <=index:
                if i==index-1:
                    curr.next=curr.next.next
                    break
                elif curr.next.next is None:
                    curr.next=None
                    break
                else:
                    curr=curr.next
                    i+=1
            return head



