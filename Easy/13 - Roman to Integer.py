#Method 1:

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman={'I':1,'V':5,'X':10,
            'L':50,'C':100,'D':500,
                'M':1000}
    
        if len(s)==0:
            return 0
        if len(s)==1:
            return roman[s[0]]
        
        i=0
        x=0
        while i<len(s):
            #print(i,s[i],roman[s[i]])
            try:
                if roman[s[i]]<roman[s[i+1]]:
                    x+=roman[s[i+1]]-roman[s[i]]
                    i+=2
                else:
                    x+=roman[s[i]]
                    i+=1
            #print(x)
            
            except:
                pass
                
                i+=1


        if roman[s[-1]]<=roman[s[-2]]:
            x+=roman[s[-1]]
        
        return x
s="III"
#s="IV"
#s="IX"
#s="LVIII"
#s="MCMXCIV"
#s="MMCDXXV"
Solution().romanToInt(s)
