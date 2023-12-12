class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_sum += nums[i]
        even_sums = []
        for i, j in queries:
            if nums[j] % 2 == 0:
                even_sum += i if i % 2 == 0 else -nums[j]
            else:
                even_sum += (i+nums[j]) if i % 2 != 0 else 0
            nums[j] = nums[j] + i
            even_sums.append(even_sum)
        return even_sums
        
        