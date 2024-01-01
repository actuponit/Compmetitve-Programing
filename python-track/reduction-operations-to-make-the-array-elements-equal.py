class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        mp = {}
        for i in nums:
            mp[i] = mp.get(i, 0) + 1
        arr = list(mp.keys())
        arr.sort()
        ans = 0
        # print(arr)
        for i in range(len(arr)-1, 0, -1):
            ans += mp[arr[i]]
            mp[arr[i-1]] += mp[arr[i]]
        return ans
