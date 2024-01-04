class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mini = min(costs)
        maxi = max(costs)
        repo = [0] * (maxi - mini + 1)
        for i in costs:
            repo[i- mini] += 1
        i, ans = 0, 0
        [2, 1, 1, 1]
        while coins > 0  and i < len(repo):
            for j in range(repo[i]):
                coins -= i + mini
                if coins < 0: break
                ans += 1
            if coins <= 0: break
            i += 1
        
        return ans
        