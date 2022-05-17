# my solution
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """

        m = 0

        for i in sentences:
            if len(i.split()) > m:
                m = len(i.split())
        return m


# fastest solution

class Solution(object):
    def mostWordsFound(self, sentences):
        maxAns = len(sentences[0].split(" "))
        lenList = len(sentences)
        for i in (sentences):
            test = len(i.split(" "))
            if(test >= maxAns):
                maxAns = test
            else:
                maxAns = maxAns
        return maxAns