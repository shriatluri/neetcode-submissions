class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Fixed sliding window technique: Look at all of the windows
        of length s1

        Have a freq array for the string s1 and the substrings in s2
        If they are ever the same for len(s1), return True
        We will lose the l index and add the r index as we move on
        '''
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        # build up both arrays for len(s1)
        for i in range(n1):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
        
        if freq1 == freq2:
            return True

        # slide window across, end of s1 to end of s2
        for i in range(n1, n2):
            # add and lose a char
            freq2[ord(s2[i]) - ord('a')] += 1
            freq2[ord(s2[i-n1]) - ord('a')] -= 1
            if freq1 == freq2:
                return True
        return False

# Time: O(n)
# Space: O(1)