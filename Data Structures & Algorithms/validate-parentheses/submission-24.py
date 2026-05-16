class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'}' : '{', ')' : '(', ']' : '['}

        for char in s:
            if char in hashmap:
                top_element = stack.pop() if stack else None
                if top_element != hashmap[char]:
                    return False
            else:
                stack.append(char)
        return not stack
