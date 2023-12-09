class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        numbers = set()
        for f, l in ranges:
            for i in range(f, l+1):
                numbers.add(i)
        r = set(range(left, right+1))
        print(numbers, r)
        return r.issubset(numbers)
        