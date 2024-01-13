class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = [-1]
        for i in range(len(nums)):
            if nums[i]%2 == 1:
                odds.append(i)
        odds.append(len(nums))
        count = 0
        for i in range(1, len(odds)-k):
            before = odds[i] - odds[i-1]
            after = odds[i+k] - odds[i+k-1]
            count += before*after
        return count