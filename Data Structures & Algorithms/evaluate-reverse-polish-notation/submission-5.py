class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                one = stack.pop()
                two = stack.pop()
                stack.append(two - one)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                one = stack.pop()
                two = stack.pop()
                stack.append(int(float(two / one)))
            else:
                stack.append(int(token))
        return stack[0]
        