import sys
sys.setrecursionlimit(10**6)

def dfs(land, i, j):
    if i < 0 or i >= N or j < 0 or j >= M or land[i][j] != 1:
        return
    land[i][j] = 0

    for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]: #상하좌우 이동
        dfs(land, i + di, j + dj)


for _ in range(int(input())):
    M, N, n = map(int, input().split())  #가로, 세로, 배추 개수
    land = [[0] * M for _ in range(N)]
    #land 구현
    for _ in range(n):
        j, i = map(int, input().split())
        land[i][j] = 1
    #배추흰지렁이 개수 count
    cnt = 0
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1:
                dfs(land, i, j)
                cnt += 1
    print(cnt)