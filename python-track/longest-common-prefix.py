class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        if not strs:
            return ""
        c = strs[0]
        for i in strs:
            if len(c) > len(i):
                c = i
        for i in range(len(c)):
            found = True
            for s in strs:
                if strs[0][i] != s[i]:
                    found = False
                    break
            if found:
                count += 1
            else: 
                break
        return strs[0][:count]

   