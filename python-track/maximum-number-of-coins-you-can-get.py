class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        i = 1
        sum = 0
        while(i<=len(piles) - len(piles)//3):
            sum += piles[i]
            i += 2
        return sum