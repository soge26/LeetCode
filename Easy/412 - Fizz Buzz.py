#Method 1:

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        x = []
        for i in range(1,n+1):
            
            if i ==1:
                x.append(str(i))
            elif i%3 == 0 and i%5 ==0:
                x.append("FizzBuzz")
            elif i%3 == 0:
                x.append("Fizz")
            elif i%5 == 0 :
                x.append("Buzz")
            else:
                x.append(str(i))
        return x
x= 15
#x= 25
Solution().fizzBuzz(x)
