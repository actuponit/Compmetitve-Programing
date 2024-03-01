class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recur(o, c, n, s):
            # print(o, c)
            # print(s)
            if o == c and o == n:
                sol.append(s)
                return
            if o > n:
                return
            if c > o:
                return
            
            recur(o+1, c, n, s+'(')
            
            recur(o, c+1,n, s+')')
        sol = []
        recur(0, 0, n, '')
        return sol

        