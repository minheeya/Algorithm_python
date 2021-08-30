class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2 #중간 인덱스
                
                if nums[mid] < target: #타겟은 중앙의 오른쪽에 위치
                    return binary_search(mid + 1, right)
                elif nums[mid] > target: #타겟은 중앙의 왼쪽에 위치
                    return binary_search(left, mid - 1)
                else:    #타겟이면
                    return mid
            else:
                return -1
        
        return binary_search(0, len(nums) - 1)
