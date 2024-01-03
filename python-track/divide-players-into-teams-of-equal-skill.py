class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        l, r = 0, len(skill)-1
        skill.sort()
        while l < r:
            ldiff = skill[l+1] - skill[l]
            rdiff = skill[r] - skill[r-1]
            if ldiff != rdiff:
                return -1
            ans += (skill[r]*skill[l])
            l += 1
            r -= 1
        return ans
        