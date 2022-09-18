class Solution :
    def twoSum (self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):  #loop in the range length of the list named nums
            for j in range (i+1, (len(nums))):
                if nums[j] == target - nums[i]:
                    return[i,j]
