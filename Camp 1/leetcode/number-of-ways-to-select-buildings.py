class Solution:
    def numberOfWays(self, s: str) -> int:
        all_ones = s.count('1')
        zeros, ones = 0, 0
        ans = 0
        for i in s:
            if i == '0':
                ans += (ones * (all_ones - ones))
                zeros += 1
            if i == '1':
                ans += (zeros * (len(s) - all_ones - zeros))
                ones += 1
        return ans