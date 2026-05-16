from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key - character freq
        # val - list of words
        freq_to_words = defaultdict(list)

        for word in strs: # O(n)
            count = [0] * 26
            for char in word: # O(m)
                count[ord(char) - ord('a')] += 1
            freq_to_words[tuple(count)].append(word)
        return list(freq_to_words.values())