class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        #재귀 함수
        def dfs(c_sum, idx, path):
            #재귀함수 종료조건 => target값 초과했을 경우
            if c_sum < 0:
                return
            #재귀함수 종료조건 => target값 일 경우
            if c_sum == 0:
                answer.append(path)
                return
            
            for i in range(idx, len(candidates)):
                dfs(c_sum - candidates[i], i, path + [candidates[i]])
            
            
        dfs(target, 0, [])
        return answer