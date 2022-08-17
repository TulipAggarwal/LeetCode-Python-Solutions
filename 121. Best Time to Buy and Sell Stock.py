class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        
        for i in range(len(prices)):
            if (buy > prices[i]): # Checking for lower buy value
                buy = prices[i] 
            elif (prices[i] - buy > profit):  # Checking for higher profit
                profit = prices[i] - buy
        return profit
