#백준 2178번
#미로탐색

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [sys.stdin.readline().rstrip() for n in range(N)]
visited = [[0]*M for n in range(N)]
move = [(-1,0), (1,0), (0,-1), (0,1)]  #위 아래 왼쪽 오른쪽 

#0,0에서 시작해서 N-1, M-1에서 끝!

q = deque([(0,0)])
visited[0][0] = 1
while q:
    x, y = q.popleft()
    if x == N-1 and y == M-1:
        print(visited[x][y])
        break
    for dx,dy in move:
        next_x, next_y = x + dx, y + dy
        if 0<=next_x<N and 0<=next_y<M :
            if maze[next_x][next_y] == '1' and not visited[next_x][next_y]:
                visited[next_x][next_y] = visited[x][y] + 1
                q.append((next_x, next_y))