class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = {}
        m = 1
        for i in s:
            mp[i] = mp.get(i, 0) + 1
            if mp[i] % 2 == 0:
                m += 2
            # else:
            #     m += max(mp[i])
        return m if m <= len(s) else m - 1