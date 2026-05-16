from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        length = 0

        for r in range(len(s)):
            count = Counter(s[l : r + 1])
            if (r - l + 1 - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
            
        
        return (r - l + 1)
