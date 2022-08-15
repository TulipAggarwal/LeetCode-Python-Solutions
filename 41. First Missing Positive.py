class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        var = nums
        hash = set(var)
        for i in range(1,length+2):
            if i not in hash:
                return i
