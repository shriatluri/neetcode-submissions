from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key - character freq
        # val - list of words
        freq_to_words = defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for char in s:
                letters[ord(char) - ord('a')] += 1
            # need to use a tuple since lists are not hashable
            freq_to_words[tuple(letters)].append(s)
        return freq_to_words.values()