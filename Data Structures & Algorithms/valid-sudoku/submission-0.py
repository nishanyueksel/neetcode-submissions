class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check all the rows
        for row in range(9):
            seen = set()
            for i in range(9):
                cell = board[row][i]
                if cell != ".":
                    if cell in seen:
                        return False
                    seen.add(cell)
        #check all columns
        for col in range(9):
            seen = set()
            for i in range(9):
                cell = board[i][col]
                if cell != ".":
                    if cell in seen:
                        return False
                    seen.add(cell)
        #check all boxes
        for box in range(9):
            seen = set()
            for row in range(3):
                for col in range(3):
                    row_idx = (box // 3) * 3 + row
                    col_idx = (box % 3) * 3 + col
                    if board[row_idx][col_idx] != ".":
                        if board[row_idx][col_idx] in seen:
                            return False
                        seen.add(board[row_idx][col_idx])
        return True
                    
