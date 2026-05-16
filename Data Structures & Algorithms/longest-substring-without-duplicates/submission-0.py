class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        L = 0
        length = 0
        for R in range(len(s)):
            while s[R] in freq:
                freq.remove(s[L])
                L += 1
            freq.add(s[R])
            length = max(length, R-L+1)
        return length