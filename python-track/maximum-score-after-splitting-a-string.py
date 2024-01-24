class Solution:
    def maxScore(self, s: str) -> int:
        prf = []
        su = 0
        for i in range(len(s) - 1, -1, -1):
            su += 1 if s[i] == '1' else 0
            prf.append(su)
        su = 0
        ans = 0
        # print(prf)
        for i in range(1, len(s)):
            su += 1 if s[i-1] == '0' else 0
            
            ans = max(su + prf[len(s) - 1 - i], ans)
        return ans
       