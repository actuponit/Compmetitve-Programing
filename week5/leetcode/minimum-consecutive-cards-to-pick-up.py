class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mini = float('inf')
        start = 0
        mp = {}
        exist = False
        for i in range(len(cards)):
            if mp and cards[i] in mp:
                mini = min(i-mp[cards[i]]+1, mini)
                exist = True
            mp[cards[i]] = i
        return mini if exist else -1