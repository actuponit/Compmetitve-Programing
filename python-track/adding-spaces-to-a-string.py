class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ''
        spaces = set(spaces)
        for i in range(len(s)):
            if i in spaces:
                ans += " " + s[i]
            else:
                ans += s[i]
        return ans
        