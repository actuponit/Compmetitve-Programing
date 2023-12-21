class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        top_right = [(0, i) for i in range(m)]
        for i in range(1, n):
            top_right.append((i, m-1))
        left_bottom = [(i, 0) for i in range(n)]
        for i in range(1, m):
            left_bottom.append((n-1, i))

        print(left_bottom, top_right)
        answer = []
        toggle = True
        for i in range(len(top_right)):
            if toggle:
                x, y = left_bottom[i]
                while y <= top_right[i][1] and x >= top_right[i][0]:
                    answer.append(mat[x][y])
                    y += 1
                    x -= 1
            else:
                x, y = top_right[i]
                while x <= left_bottom[i][0] or y >= left_bottom[i][1]:
                    answer.append(mat[x][y])
                    x += 1
                    y -= 1
            toggle = not toggle
        return answer