import math

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # last index, multiples of 1
        # second to last index, multiples of 26
        # third to last index, multiples of 676

        # ord('A') = 65

        # columnNumber = 26^x 
        # x = log_26(columnNumber)
        res = []

        while columnNumber > 0:
            columnNumber -= 1
            offset = columnNumber % 26
            res += chr(ord('A') + offset)
            columnNumber //= 26

        return ''.join(reversed(res))


            