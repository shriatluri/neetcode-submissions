class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # approach is to have key - col/row/square number and value = set
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in cols[c] or
                    board[r][c] in rows[r] or
                    board[r][c] in squares[(r//3),(c//3)]):
                    return False
                # add the proper
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3), (c//3)].add(board[r][c])
        return True

                
