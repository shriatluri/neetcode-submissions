class Solution:
    def isValid(self, s: str) -> bool:
        Map = {']':'[', '}':'{',')':'('}
        stack = []

        for c in s:
            if c in Map.keys():
                if stack and stack[-1] == Map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
            

        