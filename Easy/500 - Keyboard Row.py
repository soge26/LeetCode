#Method 1:

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row = {0: 'QWERTYUIOP', 1: 'ASDFGHJKL', 2:'ZXCVBNM'}
        
        from collections import defaultdict, Counter
        
        n1 = defaultdict(int)
        y = []
        
        for word in words:
            word=word.upper()
            [n1[letter]+0 for letter in word]
            y.append(list(n1))
            n1=defaultdict(int)
        w = []
        for i in row:
            for v,word in enumerate(y):
                x= [0 if letter not in row[i] else 1 for letter in word ]
                if all(x):
                    w.append(words[v])        
        return w

words = ["Hello", "Alaska", "Dad", "Peace"]
Solution().findWords(words)
