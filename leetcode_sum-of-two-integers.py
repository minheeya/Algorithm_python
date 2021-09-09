class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  #32bit 비트 마스크
        INT_MAX = 0x7FFFFFFF  #양수 최대값
        
        while b:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        
        if a > INT_MAX:
            a = ~(a ^ MASK)
            
        return a