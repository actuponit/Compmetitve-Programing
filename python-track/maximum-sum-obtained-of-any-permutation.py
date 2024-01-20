class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # The frequent intersection points
        repo = [0] * (len(nums) + 1)
        for i, j in requests:
            repo[i] += 1
            repo[j + 1] -= 1
        # prefix sum
        for i in range(1, len(repo)):
            repo[i] += repo[i-1]
        # the most frequent requests to the front
        repo.sort(reverse=True)
        ans = 0
        nums.sort(reverse=True)
        for i in range(len(repo)):
            if repo[i] == 0:
                break
            ans += (repo[i] * nums[i])
        return ans % ((10 ** 9) + 7)