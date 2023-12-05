class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 =="0" or num2 == "0":
            return '0'
        n = len(num1)
        m = len(num2)
        arr = [0 for _ in range(n + m)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                arr[i+j+1] += int(num1[i]) * int(num2[j])
                arr[i+j] += arr[i+j+1] // 10
                arr[i+j+1] %= 10 

        i = 0
        while arr[i] == 0:
            i += 1
        ans = ''
        while i < len(arr):
            ans += str(arr[i])
            i += 1
        return ans
"""
123
343
[ , , 1, 2, 9]
"""  
# '089910', 
# '899100'] 
# 38
# 123

#   36
#  24
# 12 
# 1476