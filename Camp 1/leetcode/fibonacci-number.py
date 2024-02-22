class Solution:
    def fib(self, n: int) -> int:
        mp = { }
        def func(n):
            if n == 1:
                return 1
            elif n == 0:
                return 0
            if n in mp:
                return mp[n]
            a = func(n-2)
            b = func(n-1)
            mp[n] = a+b 
            return a + b
        return func(n)
        