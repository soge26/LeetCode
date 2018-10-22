#Method 1:

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        A= A.split(' ')
        B= B.split(' ')
        C = []
        
        for i in A:
            if A.count(i)==1 and i not in B:
                C+=[i]
    
        for i in B:
            if B.count(i)==1 and i not in A:
                C+=[i]

                    return C

A = "this apple is sweet"
B = "this apple is sour"
#A = "apple apple"
#B = "banana banana banana"
#A="abcd def abcd xyz"
#B="ijk def ijk"
Solution().uncommonFromSentences(A, B)

#Method 2:

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        A= A.split(' ')
        B= B.split(' ')
        C = A+B
        D = []
        for i in C:
            if C.count(i)==1:
                D.append(i)
        return D

A = "this apple is sweet"
B = "this apple is sour"
#A = "apple apple"
#B = "banana banana banana"
#A="abcd def abcd xyz"
#B="ijk def ijk"
Solution().uncommonFromSentences(A, B)
