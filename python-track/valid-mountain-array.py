class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        e = -1
    
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]: return False
            if arr[i-1] > arr[i]:
                e = i
                break
        if e < 2  : return False
        for i in range(e+1, len(arr)):
            if arr[i-1] <= arr[i]:
                return False
        return True
        