class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) #value is a list
        #for each word, have a count
        for s in strs:
            count = [0] * 26 #26 letters a - z
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(s) # key = count, value = words
        return anagrams.values()


