class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # There should be a binary decision after each itteration
        res = []
        stack = []

        # Backtracking is the key here, we want to make a move and then undo and make a different move
        def backtracking(openP, closedP):
            if openP == closedP == n:
                res.append(''.join(stack))
                return
            if openP < n:
                stack.append('(')
                backtracking(openP + 1, closedP)
                stack.pop()
            if closedP < openP:
                stack.append(')')
                backtracking(openP, closedP + 1)
                stack.pop()
        
        backtracking(0, 0)
        return res

                


        