class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # [1,5,10], 12
        # min coins need to make amount a
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            # check for every coin, if there is a differnce between them
            for c in coins:
                if a - c >= 0:
                    # recursive relation
                    # Key: dp[a - c] will take to the smallest val possible
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != (amount + 1) else -1