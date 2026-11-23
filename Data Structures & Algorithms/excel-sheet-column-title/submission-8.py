import math

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # AA - 27
        # ZB - 678
        result = []
        676 / 26


        while columnNumber > 0:
            columnNumber -= 1
            charNum = (columnNumber % 26)
            print(charNum)
            result.append(chr(charNum + ord("A")))
            columnNumber //= 26
        
        result = "".join(result)
        return result[::-1]


            