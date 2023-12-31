class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        max_index = 0
        for i in range(len(names)):
            max_index = i
            for j in range(i+1, len(names)):
                if heights[j] >=  heights[max_index]:
                    max_index = j
            names[max_index], names[i] = names[i], names[max_index]
            heights[max_index], heights[i] = heights[i], heights[max_index]
        return names