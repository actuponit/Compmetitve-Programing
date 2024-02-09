class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        mp = {}
        for i in nums:
            mp[i] = 0
        start = 0
        subarrays = 0
        inc = 1
        for end in range(len(nums)):
            mp[nums[end]] += 1
            if all([i > 0 for i in mp.values()]):
                subarrays += start + 1
                while mp[nums[start]] > 1:
                    mp[nums[start]] -= 1
                    subarrays += 1
                    start += 1
        return subarrays
