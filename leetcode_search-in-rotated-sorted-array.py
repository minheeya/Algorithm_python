class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #특정 피벗을 기준으로 회전되 배열
        #최솟값의 인덱스 = 특정 피벗
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] < nums[right]: #최솟값은 mid인덱스 포함 왼쪽에 위치
                right = mid
            else:    #nums[mid] >= nums[right]일때, 최솟값은 mid인덱스 오른쪽에 위치
                left = mid + 1
        pivot = left
        
        #target값의 인덱스 찾기
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            real_mid = (mid + pivot) % len(nums) #진짜 중앙값의 위치 (모듈로 연산)
            
            if nums[real_mid] < target:
                left = mid + 1
            elif nums[real_mid] > target:
                right = mid - 1
            else:
                return real_mid
        
        return -1