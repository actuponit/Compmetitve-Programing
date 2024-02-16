class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ans = 0
        for i in s:
            if i == '(':
                stack.append('(')
            else:
                if not stack:
                    ans += 1
                else:
                    stack.pop()
        return ans + len(stack)
        