class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = defaultdict(int)
        

        for i in range(len(s1)-1, len(s2)):
            mp = Counter(s1)
            for j in range(i-len(s1)+1, i+1):
                if s2[j] in mp:
                   mp[s2[j]] -= 1 if mp[s2[j]] > 0 else 0
                else:
                    break
            if sum(mp.values()) == 0:
                return True
        return False
        