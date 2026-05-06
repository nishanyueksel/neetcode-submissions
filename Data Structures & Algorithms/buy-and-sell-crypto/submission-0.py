class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        curr_min = prices[0]
        while i < len(prices):
            curr_min = min(curr_min, prices[i])
            profit = max(prices[i] - curr_min, profit)
            i+=1
        return profit
