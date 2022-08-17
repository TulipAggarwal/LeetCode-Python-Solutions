class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for x in nums1:
            if x in nums2:
                output.append(x) #appending the element in list output
                nums2.remove(x) #removing the element to ignore double output of the same element
        return output
