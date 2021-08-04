class Solution(object):
    def threeSum(self, nums):
        
        result = []
        nums.sort()   #중복제거 간소화 하기 위해 정렬
        
        for i in range(len(nums)-2):
            #중복 일 경우 건너 뜀
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    #정답에 중복이 들어가면 X => 중복처리
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    #정답일 경우 투 포인터 이동
                    left += 1
                    right -= 1
                    
        return result