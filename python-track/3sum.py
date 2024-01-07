class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        fin = {}
        for i in range(len(nums)):
            if fin and nums[i] in fin:
                continue
            newt = -nums[i]
            mp = {}
            for j in range(i+1,len(nums)):
                tar = newt-nums[j]
                if mp and nums[j] in mp and mp[nums[j]] != None:
                    ans.append([nums[i], mp[nums[j]],  nums[j]])
                    mp[mp[nums[j]]] = None
                    mp[nums[j]] = None
                else:
                    mp[tar] = nums[j]
            fin[nums[i]] = 0
        fin = {}
        for i in range(len(ans)):
            v = sorted(ans[i])
            key = ''.join(map(str, [v[0], v[1]]))
            if fin and key in fin:
                continue
            else:
                fin[key] = ans[i]
        return list(fin.values())