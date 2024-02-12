class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        r = s % p
        mp = {0:-1}
        if r == 0: return 0
        if s < p: return -1
        s = 0
        ans = float('inf')

        for i in range(len(nums)):
            s += nums[i]
            s %= p
            if mp and ((s - r) % p) in mp:
                ans = min(ans, i-mp[(s - r) % p])
            mp[s] = i
        return ans if (ans != float('inf')) and (ans != len(nums)) else -1