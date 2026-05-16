import queue
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        length = 0
        l = 0

        for r in range(len(s)):
            if s[r] in substring:
                while s[r] in substring:
                    substring.remove(s[l])
                    l += 1

            substring.add(s[r])
            length = max(length, r - l + 1)
        
        return length

                