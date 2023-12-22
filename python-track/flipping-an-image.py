class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            s, e = 0, len(image[0])-1
            while s <= e:
                if image[i][s] == image[i][e]:
                    image[i][s] = 0 if image[i][s] == 1 else 1
                    image[i][e] = image[i][s]
                e -= 1
                s += 1
        return image
        