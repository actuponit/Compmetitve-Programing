class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #Longest word 0+26+e
        def helper(s1,  s2):
            for i in range(len(s1)):
                if len(s2) <= i:
                    return False
                if order.index(s1[i]) < order.index(s2[i]):
                    return True
                if order.index(s1[i]) > order.index(s2[i]):
                    return False
            return True
                
        for i in range(1, len(words)):
            if not helper(words[i-1], words[i]):
                return False
        
        return True
        