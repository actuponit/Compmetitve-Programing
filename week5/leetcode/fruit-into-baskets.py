class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        s = 0
        se = set()
        ans = 0
        for i in range(len(fruits)):
            se.add(fruits[i])
            if len(se) > 2:
                s = i - 1
                start = fruits[s]
                while fruits[s] == start:
                    s -= 1
                se.remove(fruits[s])
                s += 1
            ans = max(ans, i - s + 1)
        return ans

# [3,3,3,1,2,1,1,2,3,3,4]