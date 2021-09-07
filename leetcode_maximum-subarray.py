class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            #이전 값이 0보다 클 경우 더함, 또 그 값이 0보다 크면 그 다음값에 더함...(반복)
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)