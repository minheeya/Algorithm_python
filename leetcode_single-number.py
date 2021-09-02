class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            #XOR연산 입력값이 여러 개일 때, 1이 홀수 개면 1 짝수개면(0개 포함) 0 으로 결과가 나옴
            #따라서 2번씩 나오는 숫자들의 자릿수 비트는 0이 되고 1번만 나오는 숫자의 자릿수 비트는 1이 됨
            result ^= num 
        return result