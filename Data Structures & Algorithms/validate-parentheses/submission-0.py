class Solution:
    def isValid(self, s: str) -> bool:
        #use stack because a closing parantheses will be popped
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for c in s:
            if c in Map:
                if stack and stack[-1] == Map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        #only return true if stack is empty
        return not stack
