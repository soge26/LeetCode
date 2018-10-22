#Method 1:

class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        
        primes=[2, 3, 5, 7, 11, 13, 17, 19]
        
        count =0
        
        for i in range(L,R+1):
            if sum(map(int, "{0:b}".format(i))) in primes:
                count+=1
        return count
L = 10
R = 15
#L=289051
#R=294301
Solution().countPrimeSetBits(L, R)

