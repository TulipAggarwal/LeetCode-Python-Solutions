# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1
        else:
            min_good, max_bad = 1, n
            while (max_bad - min_good) > 1:
                ver = (min_good + max_bad) // 2
                if isBadVersion(ver):
                    if not isBadVersion(ver-1):
                        return ver
                    max_bad = ver
                else:
                    min_good = ver
            return max_bad
