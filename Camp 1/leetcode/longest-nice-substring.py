class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        maxi = 0
        substring = ''
        for i in range(1, len(s)):
            for j in range(i-1, -1, -1):
                # print(i, j)
                se = set(s[j:i+1])
                ans = True
                for k in se:
                    if not ((k.upper() in se) and (k.lower() in se)):
                        ans = False
                        break

                if ans and ((i - j) > maxi):
                    substring = s[j:i+1]
                    maxi = i - j

        return substring