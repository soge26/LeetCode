#Method 1:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        
        if head is None:
            return True
        
        if head.next is None:
            return True
        
        x = head
        y=[x.val]
        while x and x.next is not None:
            x=x.next
            y+=[x.val]
        
        
        return y == y[::-1]

#Method 2:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        
        if head is None:
            return True
        
        if head.next is None:
            return True
        
        x = head
        y=[x.val]
        while x and x.next is not None:
            x=x.next
            y+=[x.val]
        
        
        prev = None
        
        
        while head is not None:
            next_=head.next
            head.next=prev
            prev=head
            head = next_
        
        a = prev
        b=[a.val]
        while a and a.next is not None:
            a=a.next
            b+=[a.val]
        
        return y==b
