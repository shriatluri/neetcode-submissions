from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Get to a window that supports all the t chars properly with the same frequencies of chars by expaning the r pointer
        Increment the l while it still holds and update the min accordingly
        We will keep track of the minimum sub string and the value
        Once we hit that min window, expand r and then shrink l until the window is met
        If it is met and shorter len, update, if it is not met, keep extending r
        '''
        if t == '':
            return ''
        
        freqT = Counter(t)
        window = defaultdict(int)
        # num of chars in T
        have, need = 0, len(freqT)

        # res will be a l and r pointer
        min_sub = [-1, -1]
        min_sub_len = float('inf')

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            # we only add 1 to have if all the freq for a char are filled
            if c in freqT and window[c] == freqT[c]:
                have += 1
            
            while have == need:
                # update result (maybe)
                if (r - l + 1) < min_sub_len:
                    min_sub = [l, r]
                    min_sub_len = (r - l + 1)
                # pop from the left of the window
                window[s[l]] -= 1
                if s[l] in freqT and window[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1
        l, r = min_sub
        return s[l:r+1] if min_sub_len != float('inf') else ''
            

            

