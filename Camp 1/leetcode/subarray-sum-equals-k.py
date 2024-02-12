class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        count = 0
        d={0:1}
        # start, end = 0, 0
        # while end < len(nums):
        #     sum += nums[end]
        #     end+=1
        #     while sum > k and start < end:
        #         sum -= nums[start]
        #         start += 1
        #     if sum == k:
        #           count += 1
        for num in nums:
            sum += num
            if sum - k in d:
                count += d[sum-k]
            if not sum in d:
                d[sum] = 1
            else:
                d[sum] += 1 
        return count

                  