class Solution:
    def climbStairs(self, n: int) -> int:
        # tabulation since we only need recent 2 values
        dp = [1, 1]

        if n <= 2:
            return n
        i = 2
        while i <= n:
            # change the dp array vals
            tmp = dp[1]
            dp[1] = dp[1] + dp[0]
            dp[0] = tmp
            i += 1
        return dp[1]
