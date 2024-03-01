class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0 01 0110 01101001 0110100110010110
        if n == 1:
            return 0
        def recur(n, k):
            if n == 2 and k == 1:
                return 0
            if n == 2 and k == 2:
                return 1
            temp = 2**(n-2)
            if k > temp:
                return 0 if recur(n-1,k-temp) else 1
            else:
                return recur(n-1, k)
        return recur(n, k)

        