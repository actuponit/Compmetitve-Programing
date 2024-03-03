class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # print(matrix)
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] += matrix[i][j-1]
        # mp = defaultdict(int)
        # print(matrix)
        count = 0
        for i in range(len(matrix)):
            s = [0] * len(matrix[0])
            for k in range(i, -1, -1):
                mp = defaultdict(int)
                mp[0] = 1
                
                for j in range(len(matrix[0])):
                    if matrix[k][j]+s[j] - target in mp:
                        count += mp[(matrix[k][j]+s[j] - target)]
                    mp[matrix[k][j]+s[j]] += 1

                for j in range(len(matrix[0])):
                    s[j] += matrix[k][j]
        return count