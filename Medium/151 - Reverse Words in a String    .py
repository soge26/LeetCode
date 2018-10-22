#Method 1:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s.strip():
            return ""
        x= s.split()
        x[::-1]
        return ' '.join(x[::-1])

s = "the sky is blue"
Solution().reverseWords(s)
