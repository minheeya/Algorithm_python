class Solution:
    #swap여부 판단 함수
    @staticmethod
    def to_swap(n1, n2):
        return str(n1) + str(n2) < str(n2) + str(n1)
    
    def largestNumber(self, nums: List[int]) -> str:
        
        #삽입 정렬
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1
            
        #'00'인 경우 '0'으로 출력해야함(예외경우)
        #->int형으로 형변환 후 다시 str형으로 형변환
        return str(int(''.join(map(str, nums)))) 
     