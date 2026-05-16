class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        L, length = 0,0
        for R in range(len(s)):
            while s[R] in hashSet:
                hashSet.remove(s[L])
                L += 1
            hashSet.add(s[R])
            length = max(length, R-L+1)
        return length