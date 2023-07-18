class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k%n

        reverse (nums,0,n-1) #reversing the entire array
        reverse (nums,0,k-1) #reversing the first k elements
        reverse (nums,k,n-1) #reversing the n-k elements
