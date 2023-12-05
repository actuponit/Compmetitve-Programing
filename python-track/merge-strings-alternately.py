class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)

        arr = [""] * (l1 + l2)
        index1, index2 = 0, 0
        
        for i in range(l1 + l2):
            if index1 < l1 and i % 2 == 0:
                arr[i] = word1[index1]
                index1 += 1
            elif index2 < l2 and i % 2 == 1:
                arr[i] = word2[index2]
                index2 += 1
            elif index1 >= l1:
                arr[i] = word2[index2]
                index2 += 1
            else:
                arr[i] = word1[index1]
                index1 += 1
        return "".join(arr)