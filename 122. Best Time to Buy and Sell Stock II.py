class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [] 
        for i in range(1, len(prices)):
            profit.append(max(0, prices[i] - prices[i-1])) 
        res = sum(profit)
        return res
