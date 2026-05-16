class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for row in board:
            row_set = set()
            for tile in row:
                if tile != ".":
                    if tile in row_set:
                        return False
                    row_set.add(tile)

        
        #check columns
        for column in range(9):
            column_set = set()
            for row in range(9):
                tile = board[row][column]
                if tile != '.':
                    if tile in column_set:
                        return False
                    column_set.add(tile)
        
        #check boxes
        for box_row in range(0, 9, 3):
            for box_column in range(0, 9, 3):
                box = set()
                for row in range(3):
                    for column in range(3):
                        tile = board[box_row + row][box_column + column]
                        if tile != '.':
                            if tile in box:
                                return False
                            box.add(tile)
        
        return True
            
