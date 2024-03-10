class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        arr = []
        for i in range(1, len(weights)):
            arr.append(weights[i]+weights[i-1])
        arr.sort()
        return sum(arr[len(arr)-k+1:]) - sum(arr[:k-1])
