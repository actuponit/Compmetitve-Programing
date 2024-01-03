class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        ans = 0
        while l <= r:
            s = people[l] + people[r]
            if s <= limit:
                r -= 1
                while people[r] + s <= limit:
                    s += people[r]
                l += 1
                while people[l] + s <= limit:
                    s += people[l]
                
            else:
                r -= 1
            ans += 1
        return ans
                