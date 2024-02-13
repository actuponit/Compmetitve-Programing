class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        mp = defaultdict(list)
        for i in range(len(nums)):
            mp[nums[i]].append(i)
            nums[i] = 0
        # print(mp)
        def helper(l: List[int]):
            prefix = [l[0]] * (len(l)) 
            length = len(l)
            for i in range(1, len(l)):
                prefix[i] = prefix[i-1] + l[i]
            suffix = [0] * (len(l))
            suffix[-1] = l[-1]
            for i in range(length-1, 0, -1):
                suffix[i-1] = suffix[i] + l[i-1]
            # ans = [0] * length
            # Right
            for i in range(length - 1):
                nums[l[i]] = suffix[i+1] - ((length - i - 1) * l[i])
            # Left
            for i in range(1, length):
                nums[l[i]] += (i*l[i]) - prefix[i-1]
            
                
        for i in mp.values():
            ans = helper(i)
            
        return nums
        