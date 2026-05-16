class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #left and right pointer
        #left is buying, right is selling
        l, r = 0,1
        max_profit = 0

        while r < len(prices):
            #profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                #max of current max profit, and computed max
                max_profit = max(max_profit, profit)
            #not profitable
            else:
                #left pointer is new right pointer location
                l = r
            r += 1
        return max_profit

