class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        highest_candy = max(candies)
        for i in range(len(candies)):            
            result.append(candies[i] + extraCandies >= highest_candy)
        return result
