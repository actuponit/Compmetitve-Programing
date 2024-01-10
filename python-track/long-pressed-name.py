class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        t = 0
        r = 0 
        if len(typed) < len(name): return False
        while r < len(name):
            if typed[t] != name[r]: return False
            while  r < len(name)-1 and name[r] == name[r + 1] and typed[t] == name[r]:
                t += 1
                r += 1
            if typed[t] != name[r]: return False
            while t < len(typed) and typed[t] == name[r]:
                t += 1
            r += 1
            if len(typed) <= t:
                break
        
        return True and t == len(typed) and r >= len(name)