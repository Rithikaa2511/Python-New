class Solution(object):
    def solveSudoku(self, board):
        self.solve(board)
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for c in "123456789":
                        if self.Valid(board, i, j, c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            board[i][j] = "."
                    return False
        return True

    def Valid(self, board, i, j, c):
        for k in range(9):
            if board[i][k] == c:
                return False
            if board[k][j] == c:
                return False
            if board[3*(i//3) + k//3][3*(j//3) + k%3] == c:
                return False
        return True