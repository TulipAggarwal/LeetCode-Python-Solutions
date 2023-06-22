class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_len = 2*len(nums)+1
        new_arr = nums+nums
        return new_arr
