class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = i
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
                
        return i + 1
