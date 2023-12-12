class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(num):
            s = 0
            while num > 0:
                s += (num % 10) ** 2
                num = num // 10
            return s
        x = helper(n)
        running = 0
        while x != 1 and x != n and running < 10:
            x = helper(x)
            running += 1
        return x == 1
"""
34 
9 + 16 25
4 25 29
4 81 = 85
64 1
x2 + y2 = 1
x2 = 1 - y * 1 + y
"""