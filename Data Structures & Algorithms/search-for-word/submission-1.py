class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        # helper function to check the neighbors
        def dfs(i, k, index):
            if index == len(word):
                return True
            # make sure is in bounds
            if i < 0 or i >= rows or k < 0 or k >= cols:
                return False
            # check if it is equal to letter
            if board[i][k] != word[index]:
                return False
            # the key to this problem is to mark whenever we visit a spot, no infinite loop
            # imagine word is abababa and we have a -> b and then back to a, this is not valid
            temp = board[i][k]
            # mark all the visited nodes as *, we will change back
            board[i][k] = '*'
            # explore the next index in the word from all directions
            # if even one is true, then we return true
            next_letter = (dfs(i, k + 1, index + 1) or
                           dfs(i + 1, k, index + 1) or
                           dfs(i, k - 1, index + 1) or
                           dfs(i - 1, k, index + 1))
            # the dfs call might fail and we need to keep it for future 
            board[i][k] = temp
            return next_letter
        # only check if the first letter matches and then dfs will take care of the rest
        for i in range(len(board)):
            for k in range(len(board[0])):
                if board[i][k] == word[0]:
                    # if we hit the end of the word len, pattern for dfs is return True
                    if dfs(i, k, 0):
                        return True
        return False
