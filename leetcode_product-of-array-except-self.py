class Solution(object):
    def productExceptSelf(self, nums):
        #out = 현재위치 i를 제외한 배열의 곱
        out = []
        
        #현재위치 i를 제외한 왼쪽 배열의 곱
        p = 1
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]
        
        #i를 제외한 오른쪽 배열의 곱을 out에 곱해줌
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= p
            p *= nums[i]
        
        return out