class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def dfs(elements, start, cnt):
            #재귀함수 종료조건
            if not cnt:
                answer.append(elements[:])
                return
            
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, cnt - 1)
                elements.pop()
        
        dfs([], 1, k)
        
        return answer