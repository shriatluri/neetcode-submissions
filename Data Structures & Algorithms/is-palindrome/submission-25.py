class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ''
        for c in s:
            if c.isalnum():
                rev += c.lower()
        return rev == rev[::-1]

            

