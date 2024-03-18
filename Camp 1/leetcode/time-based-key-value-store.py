class TimeMap:

    def __init__(self):
        self.timestamps = []
        self.mp = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps.append(timestamp)
        self.mp[timestamp][key] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.mp:
            return self.mp[timestamp][key] if key in self.mp[timestamp] else ''
        ans = ''
        l, r = 0, len(self.timestamps)-1
        while l <= r:
            i = l + (r-l)//2
            if timestamp >= self.timestamps[i]:
                l = i + 1
            else:
                r = i - 1
        for j in range(r, -1, -1):
            if key in self.mp[self.timestamps[j]]:
                ans = self.mp[self.timestamps[j]][key]
                return ans

        return ans


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)