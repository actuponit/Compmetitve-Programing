class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        dd = sum([ mat[i][i] for i in range(len(mat)) ])
        ud = sum([ mat[i][len(mat)-1-i] for i in range(len(mat)) ])
        if len(mat) % 2 == 0:
            return dd + ud
        return dd + ud - mat[len(mat)//2][len(mat)//2]