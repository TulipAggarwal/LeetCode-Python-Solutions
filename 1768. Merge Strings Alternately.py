class Solution:
    def mergeAlternately(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        res = []
        
        while i < m or j < n:
            if i < m:
                res += word1[i]
                i += 1
            if j < n:
                res += word2[j]
                j += 1
        res = "".join(res)
        return res
