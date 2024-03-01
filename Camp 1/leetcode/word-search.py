class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(path, i, j, d=''):
            if len(path) == len(word):
                return True
            if (i, j) in s:
                return False
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if len(path) > len(word):
                return False
            if board[i][j] != word[len(path)]:
                return False
            path.append(board[i][j])
            t = False
            
            s.add((i, j))

            t = t or backtrack(path,i,j+1)
            t = t or backtrack(path,i,j-1)
            t = t or backtrack(path,i+1,j)
            t = t or backtrack(path,i-1,j)
            
            path.pop()
            s.remove((i, j))
            return t
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                s = set()
                if board[i][j] == word[0]:
                    if backtrack([], i, j):
                        return True
        return False
        