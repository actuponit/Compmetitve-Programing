class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        maxi = len(arr)
        ans = []
        for i in range(len(arr)-1):
            ind = arr.index(maxi)
            s = 0
            ans.append(ind+1)
            while ind > s:
                arr[ind], arr[s] = arr[s], arr[ind]
                ind -= 1
                s += 1
            ind = len(arr) - 1 - i
            s = 0 
            ans.append(ind+1)
            while ind > s:
                arr[ind], arr[s] = arr[s], arr[ind]
                ind -= 1
                s += 1
            maxi -= 1
            print(arr)
        return ans