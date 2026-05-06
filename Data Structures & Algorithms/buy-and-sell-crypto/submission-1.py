class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        maxp = 0
        for i in prices:
            maxp = max(i - low, maxp)
            if i < low:
                low = i
        return maxp


        