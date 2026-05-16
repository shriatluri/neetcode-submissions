class Solution:
    def isValid(self, s: str) -> bool:
        # add to stack if it is an open paranthesis
        # remove if closed -> open is true

        close_to_open = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        stack = []

        for c in s:
            if c not in close_to_open:
                stack.append(c)
            else:
                if stack and close_to_open[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack


