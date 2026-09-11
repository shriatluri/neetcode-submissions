class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Need a way to get frequency of each word and then map together

        Key: freq of each character, Value: the words that have that freq

        ord(char) is the int representation of a char
        '''
        groups = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            # append the word to the values of the freq key
            groups[tuple(freq)].append(word)
        return list(groups.values())