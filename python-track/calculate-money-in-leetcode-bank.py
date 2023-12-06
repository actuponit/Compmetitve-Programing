class Solution:
    def totalMoney(self, n: int) -> int:
        no_times = n // 7
        first, last = 1, 7
        idx = 0
        ans = 0
        while no_times > 0:
            
            ans += (7 * (first + last) // 2)
            first += 1
            last += 1
            no_times -= 1
        rem = n % 7
        
        for i in range(rem):
            ans += first
            first += 1

        return ans
        