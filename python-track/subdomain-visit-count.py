class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = defaultdict(int)
        for i in cpdomains:
            amount, domain = i.split()
            amount = int(amount)
            arr = domain.split('.')
            prev = ''
            for j in range(len(arr)-1, -1, -1):
                string = arr[j] + prev
                prev = '.' + string
                mp[string] += amount
        answer = []
        for key, val in mp.items():
            answer.append(str(val) + " " + key)

        return answer