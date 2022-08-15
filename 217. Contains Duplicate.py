#1st Approach:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
      
#2nd Approach:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data = set()
        for i in nums:
            if i in data:
                return True
            data.add(i)
        return False
