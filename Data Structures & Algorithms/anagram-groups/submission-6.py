class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_list = []
        hash_map = {}
        for word in strs:
            sorted_word = str(sorted(word))
            if not sorted_word in hash_map:
                hash_map[sorted_word] = [word]
            else:
                hash_map[sorted_word].append(word)

        for words in hash_map.values():
            new_list.append(words)

        return new_list

        
