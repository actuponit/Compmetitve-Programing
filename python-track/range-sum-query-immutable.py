class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tot = 0
        self.psum = [0]
        for i in nums:
            self.tot += i
            self.psum.append(self.tot)
        
        

    def sumRange(self, left: int, right: int) -> int:
        return self.psum[right+1] - self.psum[left]
            
#[0, -2, -2, 1, -4, -2, -3] -3 + 2
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)