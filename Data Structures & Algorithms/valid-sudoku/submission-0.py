class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        c0 = []
        c1 = []
        c2 = []
        # row 
        for i in range(n):
            c0.append([])
            c0[i] = [0] * (9 + 1)
            for j in range(n): 
                if board[i][j] != ".":
                    c0[i][int(board[i][j])] += 1
                    if c0[i][int(board[i][j])] > 1: 
                        print("row, ", i, j, int(board[i][j]))
                        return False

        # column 
        for i in range(n):
            for j in range(n): 
                if i == 0: 
                    c1.append([])
                    c1[j] = [0] * (9 + 1)
                if board[i][j] != ".":
                    c1[j][int(board[i][j])] += 1
                    if c1[j][int(board[i][j])] > 1: 
                        print("row, ", i, j, int(board[i][j]))
                        return False
        #grid
        for i in range(n + 1):
            c2.append([])
            c2[i] = [0] * (9 + 1)

        for i in range(n):
            for j in range(n): 
                if board[i][j] != ".":
                    c2[3 * (i//3) + j//3][int(board[i][j])] += 1
                    if c2[3 * (i//3) + j//3][int(board[i][j])] > 1: 
                        return False
        return True
            