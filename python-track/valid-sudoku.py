class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows then check cols then check each three sub grid
        mp = defaultdict(set)
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] != '.' and s and board[i][j] in s:
                    return False
                if board[i][j] != '.':
                    s.add(board[i][j])
                    if mp[j] and board[i][j] in mp[j]:
                        return False
                    mp[j].add(board[i][j])
        
        # Subgrid
        for i in range(2, len(board), 3):
            s = set()
            for j in range(2, len(board), 3):
                s = set()
                for x in range(i, i-3, -1):
                    for y in range(j, j-3, -1):
                        if s and board[x][y] in s:
                            return False
                        if board[x][y] != '.':
                            s.add(board[x][y])
        return True
            

        