class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        vertical_array = []
        max_len = 0

        for word in words:
            max_len = max(max_len, len(word))
        for letter in range(max_len):
            vertical_word = ''
            for word in words:
                if letter < len(word):
                    vertical_word += word[letter]
                else:
                    vertical_word += " "
            
            vertical_array.append(vertical_word.rstrip())
        return vertical_array
                    
