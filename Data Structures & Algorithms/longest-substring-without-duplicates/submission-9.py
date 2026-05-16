import queue
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        length = 0
        l, r = 0, 0
        substring = set()

        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            longest = max(longest, len(substring))
        
        return longest
            

                
                