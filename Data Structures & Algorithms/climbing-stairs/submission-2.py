class Solution:
    def climbStairs(self, n: int) -> int:
        # tabulation since we only need last 2 nums
        dp = [0, 1]

        if n <= 2:
            return n
        i = 2
        while i <= n:
            # change the dp array vals
            tmp = dp[1]
            dp[1] = dp[1] + dp[0]
            dp[0] = tmp
            i += 1
        return sum(dp)
