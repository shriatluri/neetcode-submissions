class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            if len(string) < 10:
                result += "1"
            elif len(string) >= 10 and len(string) < 100:
                result += "2"
            else:
                result += "3"
            
            result += "#"
            result += str(len(string))
            result += string

        print(result)

        return result


    def decode(self, s: str) -> List[str]:
        result = []
        currPos = 0
        
        if not s:
            return result

        while True:
            numCount = int(s[currPos])
            charCount = int(s[currPos + 2:currPos + 2 + numCount])
            currPos += numCount + 2

            result.append(s[currPos:currPos + charCount])
            currPos += charCount

            if currPos > len(s) - 1:
                return result


