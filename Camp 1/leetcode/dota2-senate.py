class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        radiant, dire = deque(), deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(n + r)
            else:
                dire.append(n + d)
        return "Radiant" if radiant else "Dire"
            
        