class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        list_s = list(s)
        while l != r and l < r:
            while not list_s[l].isalnum() and l < r:
                l += 1
            while not list_s[r].isalnum() and r > l:
                r -= 1
            if list_s[l].lower() == list_s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        
        return True

        