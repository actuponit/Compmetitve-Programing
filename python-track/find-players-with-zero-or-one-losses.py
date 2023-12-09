class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        mp = {
            matches[0][0]: 0
        }
        for i, j in matches:
            if not i in mp:
                mp[i] = 0
            mp[j] = mp.get(j, 0)+1
        no_loses = []
        one_lose = []
        for k, v in mp.items():
            if v == 0: no_loses.append(k)
            elif v == 1: one_lose.append(k)
        return [sorted(no_loses), sorted(one_lose)]