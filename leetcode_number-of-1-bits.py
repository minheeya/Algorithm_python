class Solution:
    def hammingWeight(self, n: int) -> int:
        #이진수에서 1을 뺀 값과 and연산 하면 비트가 1씩 빠지게 됨
        cnt = 0
        while n:  #1트씩 빠지다가 결국엔 0이 됨
            n &= n - 1
            cnt += 1
        return cnt
            
            