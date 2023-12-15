class Solution:
    def minimizedStringLength(self, s: str) -> int:
        mp = set()
        count = 0
        for i in s:
            if not (mp and i in mp):
                count += 1
            mp.add(i)
        return count