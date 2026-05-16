import queue
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        length = 0
        l, r = 0, 0

        while r < len(s):
            if (s[r] in substring):
                length = max(length, len(substring))
                while s[r] in substring:
                    substring.remove(s[l])
                    l += 1
            substring.add(s[r])
            r += 1
            
        length = max(length, len(substring))
        return length

                
                