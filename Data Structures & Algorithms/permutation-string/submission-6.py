from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        correct_list = [0 for i in range(26)]
        check_list = [0 for i in range(26)]
        matches = 0
        l = 0
        
        for i in range(len(s1)):
            correct_list[ord(s1[i]) - ord('a')] += 1

        for r in range(len(s2)):
            check_list[ord(s2[r]) - ord('a')] += 1

            if r >= len(s1):
                check_list[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if correct_list == check_list:
                return True
        
        return False

            

        
     
            
            


        
        
            

