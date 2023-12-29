class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        s = 0
        arr= []
        for i in range(1, len(flips)+1):
            s += i
            arr.append(s)
        s= 0
        count = 0
        for i in range(len(flips)):
            s += flips[i]
            if s == arr[i]:
                count += 1

        return count

        