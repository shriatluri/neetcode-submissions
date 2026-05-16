class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # need to keep track of index and values
        stack = [] # [temp, index]
        res = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append((n, i))
        return res