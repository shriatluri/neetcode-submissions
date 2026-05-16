from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26

        for char in s1:
            s1_count[ord(char) - ord('a')] += 1

        for r in range(len(s2)):
            s2_count[ord(s2[r]) - ord('a')] += 1
            if r >= len(s1):
                s2_count[ord(s2[r - len(s1)]) - ord('a')] -= 1
            
            if s1_count == s2_count:
                return True
        
        return False
            
            
            


        
        
            

