class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = [-1] * len(nums)
        st = []
        # i = 0
        c = 0
        for i in range(len(nums)):
            while st and nums[st[-1]] < nums[i]:
                arr[st[-1]] = nums[i]
                st.pop()
            
            st.append(i)
        # print(st)
        for i in range(len(nums)):
            while st and nums[st[-1]] < nums[i]:
                arr[st[-1]] = nums[i]
                st.pop()
            
            st.append(i)
        return arr