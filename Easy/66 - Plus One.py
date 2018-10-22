#Method 1:

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        x = map(str, digits)
        x = int(''.join(x)) + 1
        x = map(int, str(x))
        
        return list(x)

digits = [1,2,3]
#digits = [4,3,2,1]
Solution().plusOne(digits)


#Method 2:

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
    
        x = []
        i = -1
        
        while abs(i) <=len(digits):
            
            if digits[i]+1==10:
                digits[i]=0
            else:
                digits[i]+=1
                break
            i-=1
        
        if sum(digits)==0:
            x=[1]+digits
        else:
            x+=digits
        
        return x

digits = [1,2,3]
#digits = [4,3,2,1]
Solution().plusOne(digits)
