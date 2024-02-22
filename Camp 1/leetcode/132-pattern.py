class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mini = -1*float('inf')
        st = []
        for i in reversed(nums):
            if i < mini:
                return True
            
            while st and st[-1] < i:
                mini = st.pop()
            
            st.append(i)
        return False

        