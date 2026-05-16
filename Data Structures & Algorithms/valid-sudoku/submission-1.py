class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #key: column (0-8) value: set of digits in each column
        cols = defaultdict(set)
        #key: row (0-8) value: set of digits in each row
        rows = defaultdict(set)
        #key: tuple represening a 3x3 box value: set of digits in that box
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (
                    board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[(r//3, c//3)]
                 ):
                    return False
                #append values to each key
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[(r//3, c//3)].add(board[r][c])

        return True
