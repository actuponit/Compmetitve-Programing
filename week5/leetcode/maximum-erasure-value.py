class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = 0
        prev = set()
        sm = 0
        ans = 0
        for i in range(len(nums)):
            sm += nums[i]
            while prev and nums[i] in prev:    
                sm -= nums[s]
                prev.remove(nums[s])
                s += 1
            prev.add(nums[i])
            ans = max(ans, sm)
        return ans
            