class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # 1 2 3 4 4 4 4 4 4 4 4 4 4 5 6 7 8 
        #  6 3
        
        houses.sort()
        heaters.sort()
        def helper(num):
            j, i = 0, 0
            count = 0
            while i < len(houses) and j < len(heaters):
                val = abs(houses[i]-heaters[j])
                if val > num:
                    j += 1
                else:
                    i += 1
                if i == len(houses):
                    return True
                elif j == len(heaters):
                    return False
        r = max(abs(heaters[-1] - houses[0]), abs(heaters[0] - houses[-1]))
        l = 0
        while l <= r:
            mid = l + (r-l)//2
            if helper(mid):
                r = mid-1
            else:
                l = mid+1
        return l
        