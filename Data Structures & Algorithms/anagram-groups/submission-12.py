class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []

        while strs:
            charArray = [0 for _ in range(26)]
            word = strs[0]
            anagramList = [word]

            for char in word:
                charArray[ord(char.lower()) - ord('a')] += 1

            for checkWord in strs[1:]:
                checkCharArray = [0 for _ in range(26)]
                for char in checkWord:
                    checkCharArray[ord(char.lower()) - ord('a')] += 1
                
                if charArray == checkCharArray:
                    strs.remove(checkWord)
                    anagramList.append(checkWord)
            
            strs.remove(word)
            result.append(anagramList)
        
        return result




