from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        count = {}
        length = 0

        for r in range(len(s)):
            count = Counter(s[l:r + 1])

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            length = max(length, r - l + 1)
        
        return length

            
        return length