from collections import defaultdict
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return nums[0]
        
        dp = defaultdict(int)  #dp[i] = i지점까지 훔친 돈의 최대 액수
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)): 
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[len(nums) - 1]