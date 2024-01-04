class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        j = 0
        s.sort()
        g.sort()
        for i in range(len(g)):
            while j < len(s) and g[i] > s[j]:
                j += 1
            if j == len(s):
                break
            count += 1
            j += 1
        return count