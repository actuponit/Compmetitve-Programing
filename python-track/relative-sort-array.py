class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        size = max(arr1) - min(arr1) + 1
        offset = min(arr1)
        storage = [0] * size
        for i in range(len(arr1)):
            storage[arr1[i] - offset] += 1

        t = 0
        for i in arr2:
            for j in range(storage[i-offset]):
                arr1[t] = i
                t += 1
            storage[i-offset] = 0
        # print(s)
        for i in range(len(storage)):
            for j in range(storage[i]):
                arr1[t] = i+offset
                t += 1

        return arr1
        