class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0

        left, right = 0, 1
        max_profit = 0

        while right < len(prices):

            subtract = prices[right] - prices[left]

            if subtract < 0:
                left = right
            
            max_profit = max(subtract, max_profit)

            right += 1
        
        return max_profit



        