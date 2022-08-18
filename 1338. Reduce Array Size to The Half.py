class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        remove = 0
        nums = collections.Counter(arr)  # using collections.Counter here to determine the frequency count of each element in the array
        values = sorted(nums.values(), reverse = True) # using sorted() to sort the nums array in reverse order
        length = len(arr)  
        rem = length//2  
        for count in values:
            rem -= count # removing count from half length of array arr
            remove +=1 # counting remove variable as +1 in each iteration
            if rem<=0:
                return remove 
