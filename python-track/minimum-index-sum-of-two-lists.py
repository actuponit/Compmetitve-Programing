class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        mp ={}
        min_sum = float('inf')
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    mp[list1[i]] = i+j
                    min_sum = min(min_sum, i+j)
                    break
        for key, value in mp.items():
            if value == min_sum:
                ans.append(key)

        return ans