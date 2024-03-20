class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-1
        while l <= r:
            mid = (l+r) // 2
            if arr[mid] >= x:
                r = mid - 1
            else:
                l = mid + 1
        arr1 = arr[:l]
        arr2 = arr[l:]
        p1, p2 = l-1, 0
        ans = []
        print(arr1)
        print(arr2)
        while k > 0:
            if p1 < 0 and p2 < len(arr2):
                ans.append(arr2[p2])
                p2 += 1
                k -= 1
                continue
            if p1 >= 0 and p2 >= len(arr2):
                ans.append(arr1[p1])
                p1 -= 1
                k -= 1
                continue
            if p1 < 0 and p2 >= len(arr2):
                break
            if abs(arr2[p2] - x) >= abs(arr1[p1] - x):
                ans.append(arr1[p1])
                p1 -= 1
            else:
                ans.append(arr2[p2])
                p2 += 1
            k -= 1
        ans.sort()
        return ans

