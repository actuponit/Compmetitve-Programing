class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [len(temperatures)-1]
        ans = [0]
        for i in range(len(temperatures)-2, -1, -1):
            #if temperatures[i] < temperature[stack[-1]]:      
            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1] - i)
            stack.append(i)
        return ans[::-1]
            



"""
st   6 5 5 6 2 1
te 6 5 4 3 2 1 0
 ans 0 0 6-5 5-4 5-3 6-2 2-1 1-0
1 1 4 2 1 1 0 0
st 73 76 72 69 72 71 72 
te 76 72 69 71 71 75 75
an 0  1  1     2
"""
