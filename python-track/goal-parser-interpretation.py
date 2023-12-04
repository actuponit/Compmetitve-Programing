class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        i = len(command)-1
        while i > -1:
            if command[i] == ')':
                i -= 1
                val = 'o'
                while command[i] != '(':
                    i -= 1
                    val = 'al'
            else:
                val = 'G'
            i -= 1
            ans = val + ans
        return ans
                
        