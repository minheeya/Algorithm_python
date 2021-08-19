class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def dfs(idx, path):
            answer.append(path)
            
            for i in range(idx, len(nums)):
                dfs(i + 1, path + [nums[i]])
        
        dfs(0, [])
        return answer