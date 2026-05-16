class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # the approach for this is to backtrack
        # we should only add an open < n and a closed < open for valid
        res = []
        stack = []

        # stack which will keep track of the current itteration

        def backtrack(num_open, num_closed):
            if num_open == num_closed == n:
                # the finla string
                res.append(''.join(stack))
                return
            if num_open < n:
                stack.append('(')
                backtrack(num_open + 1, num_closed)
                stack.pop()
            if num_closed < num_open:
                stack.append(')')
                backtrack(num_open, num_closed + 1)
                stack.pop()
        backtrack(0,0)
        return res