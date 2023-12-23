class Robot:

    def __init__(self, width: int, height: int):
        self.width = width-1
        self.height = height-1
        self.directions = ["East", "North", "West", "South"]
        self.steps = 0

    def step(self, num: int) -> None:
        self.steps += num
        cycle = self.width*2 + self.height*2
        self.steps = cycle if self.steps % cycle == 0 else self.steps % cycle 
        print(self.steps)

    def getPos(self) -> List[int]:
        arr = [self.width, self.height, self.width, self.height]
        i = 0
        step = self.steps
        while i < len(arr):
            if  step > arr[i]:
                step -= arr[i]
            else:
                break
            i += 1
        if i == 0:
            return [step, 0]
        if i == 1:
            return [self.width, step]
        if i == 2:
            return [self.width-step, self.height]
        if i == 3:
            return [0, self.height-step]
         

    def getDir(self) -> str:
        arr = [self.width, self.height, self.width, self.height]
        i = 0
        step = self.steps
        while i < len(arr)-1:
            if  step > arr[i]:
                step -= arr[i]
            else:
                break
            i += 1
        return self.directions[i]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()