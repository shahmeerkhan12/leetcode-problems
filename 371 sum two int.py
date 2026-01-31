class Solution:
    def getSum(self, a: int, b: int) -> int:
        m = 0xFFFFFFFF
        while b != 0:
            temp = (a^b) & m
            b = ((b & a) << 1) & m
            a = temp
        return a if a<= 0x7FFFFFFF else ~(a^m)
