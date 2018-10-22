#Method 1:

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        import math
        if math.sqrt(n).is_integer():
            return 1
        
        def nums(n):
            i = n
            def nearestsquare(n):
                
                x = math.sqrt(n)
                y = math.floor(x)
                z = y*y
                
                return(z)
            
            squarelist = []
            while i >0:
                t= nearestsquare(i)
                squarelist.append(t)
                i=t-1
            
            return squarelist
        
        def twoSum(nums, target):
            from collections import OrderedDict
            i = 0
            
            while i <= len(nums)-1:
                x = (target-nums[i])

                if x in nums and nums.index(x) != i:
                    return True
                else:
                    i+=1
        
        sqlist = nums(n)
        i=0
        j=0
        
        path = n
        
        
        for i in sqlist:
            
            count = 0
            rem = n
            j=sqlist.index(i)
            
            #print('i',i)
            while rem!=0:
                
                #print('j:',j)
                try :
                    #print('remainder:',rem, 'count:',count)
                    
                    if path < count:
                        break
                
                    r= [s for s in sqlist if s<rem]
                    
                    if twoSum(r,rem) == True:
                        count +=2
                        break
        
                    if rem in sqlist:
                        count+=1
                            break
                        
                    if rem < sqlist[j]:
                        
                        #print('rem smaller',rem,'sqlist[j]',sqlist[j])
                        if rem - sqlist[j+1]<0:
                            j+=1
                        else:
                            #print('ok')
                            j+=1
                            rem -= sqlist[j]
                            count+=1
                    else:
                        rem -= sqlist[j]
                        count+=1
                    
                except:
                    
                    #print('remainder.....:',rem)
                    break
            if count<path:
                path = count
        return(path)

x= 42
x=76
Solution().numSquares(x)


