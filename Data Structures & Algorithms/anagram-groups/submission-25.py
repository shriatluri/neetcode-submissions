from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # "a" = 97
        wordMatches = defaultdict(list)

        for word in strs:
            alphabet = [0] * 26
            for char in word:
                alphabet[ord(char) - 97] += 1
            
            wordMatches[tuple(alphabet)].append(word)

        return list(wordMatches.values())
                
