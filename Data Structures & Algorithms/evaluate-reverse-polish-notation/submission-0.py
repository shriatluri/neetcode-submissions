class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #the stack will always be the length of one digit
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == '*':
                stack.append(stack.pop()* stack.pop())
            elif c == '/':
                a,b = stack.pop(), stack.pop()
                #integer division and round to 0
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]
                 