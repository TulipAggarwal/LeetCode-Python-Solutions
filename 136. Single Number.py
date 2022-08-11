class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singlenum = 0
        for i in range(len(nums)):
            singlenum ^= nums[i]
        return singlenum
