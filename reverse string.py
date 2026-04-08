class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        if k==1: return s

        subs = s[:k]
        rev = "".join(reversed(subs))
        return rev + s[k:]
        
    
