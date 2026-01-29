class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = int(a,2)
        n2 = int(b,2)
        s = n1 + n2
        return bin(s).replace("0b","")
