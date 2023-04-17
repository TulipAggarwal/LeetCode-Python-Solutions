class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = ""
        for i in zip(*strs):
            if len(set(i)) == 1: 
                a += i[0]
            else: 
                return a
        return a
