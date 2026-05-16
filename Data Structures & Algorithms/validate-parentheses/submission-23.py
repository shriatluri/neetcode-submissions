class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char in parMap:
                top_element = stack.pop() if stack else None
                if top_element != parMap[char]:
                    return False
            else:
                stack.append(char)
        return not stack
                