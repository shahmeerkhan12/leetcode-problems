class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxLen = max(len(a),len(b))
        a = a.zfill(maxLen)
        b = b.zfill(maxLen)
        
        carry = 0
        result = []

        for i in range(maxLen - 1, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b[i])

            total = bit_a + bit_b + carry
            result.append(str(total % 2))
            carry = total // 2

        if carry:
            result.append('1')
    
        # Reverse and join
        return ''.join(result[::-1])
