class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        e = len(digits) - 1
        if digits[e] < 9:
            digits[e] += 1
            return digits
        while e > -1 and digits[e] == 9:
            digits[e] = 0
            e -= 1
            if e == -1:
                digits.append(0)
                digits[0] = 1
                return digits        
            
        digits[e] += 1
        
        return digits
"""
"""