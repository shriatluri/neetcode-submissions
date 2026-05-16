import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        lowest_price = math.inf
        l = 0

        for i in range(len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            
            profit = prices[i] - lowest_price
            
            if profit > max_profit:
                max_profit = profit

        return max_profit