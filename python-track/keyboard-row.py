class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        first_letter = words[0][0]
        def helper(letter):
            if letter.lower() in "qwertyuiop":
                return 1
            elif letter.lower() in "asdfghjkl":
                return 2
            else:
                return 3
        answer = []

        for i in words:
            #First letter to determine group
            group = helper(i[0])
            append = True
            for j in i:
                if helper(j) != group:
                    append = False
                    print(j, helper(j))
                    break
                    
            if append: answer.append(i)
        return answer
        