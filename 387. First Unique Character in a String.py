class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s) #building hash map
        for var,i in enumerate(s):
            if count[i] == 1:
                return var
        return -1
