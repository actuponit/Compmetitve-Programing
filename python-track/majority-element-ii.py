class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = {}
        for i in nums:
            mp[i] = mp.get(i, 0) + 1
        limit  = len(nums) // 3
        ans = []
        for i in mp.keys():
            if mp[i] > limit:
                ans.append(i)
        return ans