class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute force is to just look at every single possible combination

        # Sliding window technique
        # keep track of the len of the window which is one character + k
            # (right - left + 1) - maxFreq <= k
        # shrink if we exeed that limit
        # return the longest window found

        count = {}
        res = 0
        l = 0
        maxFreq = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            # max freq of that window
            maxFreq = max(maxFreq, count[s[r]])
            if (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res