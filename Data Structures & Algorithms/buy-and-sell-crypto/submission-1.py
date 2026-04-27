class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # right > left 移動 right
        # left > right -> 移動 left
        if len(prices) < 2:
            return 0
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit >= 0:
                right += 1
            elif profit < 0:
                left += 1
                if left == right:
                    right += 1

            max_profit = max(max_profit, profit)
        
        return max_profit
            

        