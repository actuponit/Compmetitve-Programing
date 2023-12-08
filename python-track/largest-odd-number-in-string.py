class Solution:
    def largestOddNumber(self, num: str) -> str:
        flag = False
        ans = ''
        for i in range(len(num)-1, -1, -1):
            if flag:
                ans = num[i] + ans
            elif int(num[i]) % 2 == 1:
                flag = True
                ans = num[i]
        return ans