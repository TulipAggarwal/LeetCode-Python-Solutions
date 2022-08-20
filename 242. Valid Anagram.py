class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lists = list(s)
        listt = list(t)
    
        lists.sort()
        listt.sort()
        
        if lists == listt:
            return True
        else:
            return False
