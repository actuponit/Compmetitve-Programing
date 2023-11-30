class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        # Vertical
        for c in range(n):
            j = 0
            i = c
            comp = matrix[i][j]
            while i < n and j < m:    
                if matrix[i][j] != comp:
                    return False
                i += 1
                j += 1
        #Horizontal
        for c in range(1, m):
            j = c
            i = 0
            comp = matrix[i][j]
            while i < n and j < m:
                if matrix[i][j] != comp:
                    return False
                i += 1
                j += 1
        return True