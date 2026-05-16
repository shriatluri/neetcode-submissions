class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #mapping character count to the list of anagrams
        res = defaultdict(list)

        for s in strs:
            #count how many of each character
            count = [0] * 26
            for c in s:
                #counting how many of each character
                count[ord(c) - ord('a')] += 1
            #appending the string s
            res[tuple(count)].append(s)
            
        return res.values()