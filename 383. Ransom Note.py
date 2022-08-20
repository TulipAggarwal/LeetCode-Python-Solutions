class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list=[]
        for i in magazine:
            list.append(i)
        for i in ransomNote:
            if i in list:
                list.remove(i)
            elif i not in list:
                return False
        return True
