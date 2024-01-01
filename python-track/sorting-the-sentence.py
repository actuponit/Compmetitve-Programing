class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(" ")
        arr.sort(key = lambda e: int(e[len(e)-1]))
        output = ""
        for i in range(len(arr)):
            char = str(i+1)
            word = arr[i].replace(char, "")
            if i != len(arr)-1:
                output += word + " "
            else:
                output += word
            
        return output
            
        