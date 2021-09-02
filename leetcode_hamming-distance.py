class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #x^y는 10진수로 반환 -> bin(10진수)는 10진수를 2진수로 표현한 문자열 반환
        #XOR은 두 비트가 다를 때 1
        return bin(x^y).count('1')