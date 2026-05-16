class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Keep a set and make it a sliding window
        l = 0
        curSet = set()
        res = 0

        for r in range(len(s)):
            # keep removing s[r] until valid
            while s[r] in curSet:
                curSet.remove(s[l])
                l += 1
            curSet.add(s[r])
            res = max(res, len(curSet))
        return res