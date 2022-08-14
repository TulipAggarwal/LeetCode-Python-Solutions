#1st approach:
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Sum = sum(nums)
        lsum = 0
        for i,x in enumerate (nums):
            if lsum == ( Sum - lsum - x):
                return i
            lsum += x  
        return -1
   

#2nd approach:
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = 0
        rsum = 0
        for i in range(1,len(nums)):
            lsum = sum(nums[0:i])
            rsum = sum(nums[i+1:])
            if lsum == rsum:
                return i
        return -1
      
 
