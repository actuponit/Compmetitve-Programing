class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # [0, 0, 1, 0]
        # [0, 1, 2, 2, 3]
        # [1, 1, 1, 0, 0]
        left = [0]*(len(nums)+1)

        for i in range(len(nums)):
            if nums[i] == 0:
                left[i+1] += left[i] + 1
            else:
                left[i+1] = left[i]
        right = [0]*(len(nums)+1)
    
        for i in range(len(nums)-1, -1, -1):
            right[i] = nums[i] + right[i+1]
            
        maxi = -1
        for i in range(len(left)):
            maxi = max(maxi, left[i]+right[i])
        answer = []
        for i in range(len(left)):
            if left[i]+right[i] == maxi:
                answer.append(i)
        return answer