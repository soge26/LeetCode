#Method 1:

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        
        d= dict(zip(list("abcdefghijklmnopqrstuvwxyz"),widths))
        count = 0
        line=0
        i=0
        
        while i<len(S):

            if count+d[S[i]]==100:
                count=0
                line+=1
                i+=1
            
            elif count+d[S[i]]>100:
                
                count=d[S[i]]
                line+=1
                i+=1
            
            else:
                count+=d[S[i]]
                i+=1
    
        line+=1
        return [line, count]

widths=[7,5,4,7,10,7,9,4,8,9,6,5,4,2,3,10,9,9,3,7,5,2,9,4,8,9]
S="zlrovckbgjqofmdzqetflraziyvkvcxzahzuuveypqxmjbwrjvmpdxjuhqyktuwjvmbeswxuznumazgxvitdrzxmqzhaaudztgie"
#widths = [7,5,4,7,10,7,9,4,8,9,6,5,4,2,3,10,9,9,3,7,5,2,9,4,8,9]
#S = "aabbccddeaabbccdde"
Solution().numberOfLines(widths, S)
