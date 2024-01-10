class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = sum(nums[:k]) / k
        ans = avg
        print(avg)
        for i in range(k, len(nums)):
            avg += nums[i] / k
            avg -= nums[i-k] / k
            ans = max(avg, ans)
        return ans
        