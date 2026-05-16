class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        occurancesS = {}
        occurancesT = {}
        for i in range(len(s)):
            occurancesS[s[i]] = 1 + occurancesS.get(s[i], 0)
            occurancesT[t[i]] = 1 + occurancesT.get(t[i], 0)
        return occurancesS == occurancesT
        