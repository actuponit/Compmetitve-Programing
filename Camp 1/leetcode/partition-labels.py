class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        for i in range(len(s)):
            m[s[i]] = i
        ma = m[s[0]]
        st = 0
        ans = []
        for i in range(len(s)):
            if i == ma:
                ans.append(ma - st + 1)
                st = i + 1 if (i+1) < len(s) else 0
                ma = m[s[st]]
            else:
                ma = max(ma, m[s[i]])
        return ans