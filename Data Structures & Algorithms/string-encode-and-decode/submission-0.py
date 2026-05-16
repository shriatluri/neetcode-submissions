class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        #each iteration of the loop will read one word
        while i < len(s):
            j = i
            #keep incrementing until # is found
            #until j is at #
            while s[j] != '#':
                j += 1
            #how many following characters to read after j
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
            