class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        result = 0
        substring = set()

        while r < len(s):
            currChar = s[r]

            if currChar in substring:
                while currChar in substring:
                    substring.remove(s[l])
                    l += 1
            
            substring.add(currChar)
            r += 1
            result = max(result, len(substring))
        
        return result

        



        