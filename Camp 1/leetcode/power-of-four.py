class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power(x):
            if x < 4:
                return x == 1.0
            return power(x/4)
        return power(n)

"""
power(5) -> power(1.25) -> false
power(4) -> power(1) -> True
power(1) -> True
if n < 4
return Ture if n == 1 else False
power(n/4)
16 // 4 4
4/4 1


"""