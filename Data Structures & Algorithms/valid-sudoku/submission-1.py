class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            visited_row = set()
            for j in range(len(board)):
                if board[i][j] != ".":
                    rnum = board[i][j]
                    if rnum in visited_row:
                        return False
                    visited_row.add(rnum)
        
        for i in range(len(board)):
            visited_col = set()
            for j in range(len(board)):
                if board[j][i] != ".":
                    rnum = board[j][i]
                    if rnum in visited_col:
                        return False
                    visited_col.add(rnum)

        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                box_visited = set()
                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        if board[row][col] != ".":
                            box_num = board[row][col]
                            if box_num in box_visited:
                                return False 
                            box_visited.add(box_num)                            

        return True