class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0

        profit = 0
        left, right = 0, 1
        
        while right < len(prices):
            if right - left <= 0:
                right += 1
                continue

            if prices[right] - prices[left] < 0:
                left = right
            
            profit = max(prices[right] - prices[left], profit)
            right += 1
        
        return profit
            




        