class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        for i in set(nums):
            if nums.count(i) > 2:
                for j in range (nums.count(i)-2):
                    nums.remove(i)
                    length -= 1
        return length
