#Method 1:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if not headA:
            return None
        
        if not headB:
            return None
        
        tmp1 = headA
        size1=0
        tmp2= headB
        size2=0
        
        while tmp1.next is not None:
            tmp1 = tmp1.next
            size1+=1
        
        while tmp2.next is not None:
            tmp2 = tmp2.next
            size2+=1
        
        
        if tmp1!=tmp2:
            return None
        
        else:
            tmp1 = headA
            tmp2= headB
            
            x=abs(size1-size2)
            if size1>size2:
                for i in range(x):
                    tmp1=tmp1.next
        
            elif size1<size2:
                for i in range(x):
                    tmp2=tmp2.next
            
            while True:
                if tmp1==tmp2:
                    return tmp1
                else:
                    tmp1=tmp1.next
                    tmp2=tmp2.next



