class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        c = capacity
        for i in range(len(plants)):
            if c < plants[i]:
                ans += 2*i + 1
                c = capacity
            else:
                ans += 1
            c -= plants[i]
        return ans

        