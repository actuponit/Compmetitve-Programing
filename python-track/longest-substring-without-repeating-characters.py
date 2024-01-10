class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first, end = 0, 1
        ans = 0
        while end < len(s):
            if s[end] in s[first:end]:
                while first < end and s[first]!=s[end]:
                    first += 1
                first += 1
            end += 1
            ans = max(ans, end - first)
        return 1 if len(s) == 1 else ans 
