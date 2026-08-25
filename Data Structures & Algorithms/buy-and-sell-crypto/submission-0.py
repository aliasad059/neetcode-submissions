class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0

        for p in prices: 
            max_profit = max(max_profit, p - lowest)
            lowest = min(lowest, p)
        
        return max_profit