class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue

                # check row
                for i, value in enumerate(board[row]):
                    if board[row][col] == value and not i == col:
                        return False
                
                # check column
                for i, rowVals in enumerate(board):
                    if board[row][col] == rowVals[col] and not i == row:
                        return False
                
                # check square
                squareColSection = 0
                squareRowSection = 0
                if col <= 2:
                    squareColSection = 3
                elif col <= 5:
                    squareColSection = 6
                else:
                    squareColSection = 9
                
                if row <= 2:
                    squareRowSection = 3
                elif row <= 5:
                    squareRowSection = 6
                else:
                    squareRowSection = 9
                
                for squareRow in range(squareRowSection - 3, squareRowSection):
                    for squareCol in range(squareColSection - 3, squareColSection):
                        if board[row][col] == board[squareRow][squareCol] and (squareRow != row or squareCol != col):
                                return False
        
        return True




