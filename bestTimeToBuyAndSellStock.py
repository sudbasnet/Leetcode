class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        buyAt = 0
        
        for i in range(1, len(prices)):
            if prices[i] - prices[buyAt] > profit:
                profit = prices[i] - prices[buyAt]
            if prices[i] < prices[buyAt]:
                buyAt = i
        
        return profit