#1st approach
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        arr.append(nums[0])
        for index in range (1,len(nums)):
            nums[index] += nums[index - 1]
            arr.append(nums[index])
        return (arr)
      
#2nd approach
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for index in range (1,len(nums)):
            nums[index] += nums[index - 1]  
        return (nums)
