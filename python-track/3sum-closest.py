class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mini = 13001
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            s = float('inf')
            while j < k:
                if abs(target - s) > abs(target - (nums[i] + nums[j] + nums[k])): 
                    s = nums[i] + nums[j] + nums[k]

                if nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < target:
                    j += 1
                else:
                    return target

            if abs(target - s) < mini:
                mini = abs(target - s)
                ans  = s
        return ans