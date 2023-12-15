class FrequencyTracker:

    def __init__(self):
        self.frequencies = defaultdict(int)
        self.values = defaultdict(int)

    def add(self, number: int) -> None:
        self.values[self.frequencies[number]] -= 1 if self.values[self.frequencies[number]] > 0 else 0
        self.frequencies[number] += 1
        self.values[self.frequencies[number]] += 1
        
    def deleteOne(self, number: int) -> None:
        self.values[self.frequencies[number]] -= 1 if self.values[self.frequencies[number]] > 0 else 0
        self.frequencies[number] -= 1 if self.frequencies[number] > 0 else 0
        self.values[self.frequencies[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.values and self.values[frequency] > 0
            
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)