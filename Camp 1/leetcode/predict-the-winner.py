class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def predict(l, r):
            if l == r:
                return nums[l]
            if l > r:
                return 0
            left = nums[l] + min(predict(l+2, r), predict(l+1, r-1))
            right = nums[r] + min(predict(l, r-2), predict(l+1, r-1))
            return max(left, right)
        # print(predict(0, len(nums) - 1))
        print(1.0 == 1)
        return predict(0, len(nums) - 1) >= (sum(nums) / 2)
        