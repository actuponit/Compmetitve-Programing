class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = defaultdict(int)
        if len(t) > len(s): return ""
        for i in t:
            mp[i] += 1
        st = 0
        ans = [0, len(s)]
        found = False
        for i in range(len(s)):
            if s[i] in mp:
                mp[s[i]] -= 1

            while all([j<=0 for j in mp.values()]):
                found = True
                if ans[1] - ans[0] > i - st:
                    ans = [st, i]
                if s[st] in mp:
                    mp[s[st]] += 1
                st += 1

        return s[ans[0]:ans[1]+1] if found else ""