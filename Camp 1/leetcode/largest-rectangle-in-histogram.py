class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        arr = [-1] * len(heights)
        mp = defaultdict(lambda : [0, 0])
        st = [-1]
        for i in range(len(heights)):
            while st[-1] != -1 and heights[st[-1]] > heights[i]:
                val = st.pop()
                mp[val][1] = i-val-1
            mp[i][0] = i-st[-1]-1
            mp[i][1] = len(heights)-i-1
            st.append(i)
        for key, val in mp.items():
            arr[sum(val)] = max(arr[sum(val)], heights[key])
        ans = 0
        curr = 0
        
        for i in range(len(arr)-1, -1, -1):
            if arr[i] != -1:
                ans = max(ans, arr[i]*(i+1))
        return ans
