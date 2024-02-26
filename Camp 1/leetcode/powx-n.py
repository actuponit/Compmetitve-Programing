class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(i, j):
            if j < 0:
                j = -1*j
                i = 1/i
            if i == 1 or j == 0:
                return 1
            elif j == 1:
                return i
            elif j%2 == 0:
                return pow(i*i, j//2)
            else:
                return i*pow(i, j-1)
        return pow(x, n)