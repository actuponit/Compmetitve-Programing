class Solution:
    def smallestNumber(self, num: int) -> int:
        arr = []
        negative = False
        if num < 0:
            negative = True
            num *= -1
        while num > 0:
            arr.append(num % 10)
            num = num // 10
        if negative:
            arr.sort(reverse=True)
        else:
            arr.sort()
            i = 0
            while i < len(arr) and arr[i] == 0:
                i += 1
            if i < len(arr):
                arr[i], arr[0] = arr[0], arr[i]
        ans = 0
        for i in range(len(arr)):
            ans += arr[i] * (10 ** (len(arr)-1-i))

        return -1*ans if negative else ans
