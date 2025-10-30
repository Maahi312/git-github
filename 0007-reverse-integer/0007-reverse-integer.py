class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        reversed_str = str(x)[::-1]
        reversed_num = int(reversed_str) * sign    
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            reversed_num = 0    
        return reversed_num