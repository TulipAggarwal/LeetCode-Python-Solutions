class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso_map = {}
#in zip function an iterator of tuples where the first item in each passed iterator is paired together
        for s1, t1 in zip(s,t): 
            if s1 not in iso_map:
                iso_map[s1] = t1
            elif iso_map[s1] != t1:
                return False
        return len(set(iso_map.values())) == len(iso_map.values())
