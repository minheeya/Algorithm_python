# Lower bound
# 정렬 된 배열(nums)에서 찾고자 하는 값(target) 이상이 처음 나타나는 위치
# nums[k-1] < target 이고 nums[k] >= target인 k를 찾는다

def lower_bound(nums, target):
    
    left, right = 0, len(nums)
    
    while left < right:  #left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = left + (right - left) // 2
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return right


# Upper bound
# 정렬 된 배열(nums)에서 찾고자 하는 값(target)보다 큰 값이 처음 나타나는 위치
# nums[k] > target 을 만족하는 최소 k를 찾는다

def upper_bound(nums, target):

    left, right = 0, len(nums)

    while left < right:  #left와 right가 만나는 지점이 target값 보다 큰 값이 처음 나오는 위치
        mid = left + (right - left) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid 

    return right


if __name__ == '__main__':
    nums = [1,2,2,2,3,5,6,8,9]
    print(lower_bound(nums, 3))   #4
    print(upper_bound(nums, 3))   #5
