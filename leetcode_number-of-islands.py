class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        #중첩함수
        def dfs(i, j):
            #값이 '1'이 아니거나 범위를 벗어나면 종료
            if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])) or grid[i][j] != '1':
                return
            
            grid[i][j] = '0'  #다시 방문하지 않도록 값 변경
            
            #동서남북으로 재귀 호출
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
                    
        return cnt
