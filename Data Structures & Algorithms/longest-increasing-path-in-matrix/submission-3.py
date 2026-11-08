class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # no need for visited as same numbers will not be put in the path as there is no strict increase
        def get_path(r, c, matrix, best_matrix):
            if (best_matrix[r][c] > 0):
                return best_matrix[r][c]
            l = 1
            paths = {(r-1, c), (r+1, c), (r, c-1), (r, c+1)}
            for p in paths:
                row = p[0]
                col = p[1]
                if (row<0 or col<0 or col >len(matrix[0])-1 or row > len(matrix)-1):
                    continue

                if (matrix[r][c] < matrix[row][col]):
                    if (best_matrix[row][col] > 0):
                        l = max(l, 1+best_matrix[row][col])
                    else:
                        l = max(l, 1+get_path(row, col, matrix, best_matrix))
            best_matrix[r][c] = l
            return l

        max_len = 0
        best_matrix = []
        for r in range(len(matrix)):
            best_matrix.append([])
            for c in range(len(matrix[0])):
                best_matrix[r].append(0)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                n = get_path(r, c, matrix, best_matrix)
                
                max_len = max(max_len, n)
        return max_len