# 2020카카오인턴십_경주로건설
# 문제를 보려면 다음 링크로 들어가세요 https://programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

def solution(board):
    N = len(board)
    answer = N*N*100 + N*N*500
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited = {(0, 0, 0): 0, (0, 0, 1): 0, (0, 0, 2):0, (0, 0, 3):0}    # (x,y,d : cost)
    q = deque([(0,0,-1,0)])   #x좌표, y좌표, 방향, 비용

    while q:
        x, y, d, cost = q.popleft()

        for next_d in range(4):  # 0:위, 1:왼쪽, 2:아래, 3:오른쪽
            next_x = x + dx[next_d]
            next_y = y + dy[next_d]
            next_cost = cost
            if (-1 < next_x < N) and (-1 < next_y < N) and not board[next_x][next_y]:

                if d == -1:  #처음 출발 방향은 -1로 정의
                    next_cost += 100
                elif (d - next_d) % 2 == 0: #평행
                    next_cost += 100
                else:   #직각
                    next_cost += 600
                
                if next_x == N-1 and next_y == N-1: #도착했을경우
                    answer = min(answer, next_cost)
                    break

                # 방문한적없음 or  같은 곳을 더 적은 비용으로 방문했을경우
                if (visited.get((next_x, next_y, next_d)) is None) or (visited[(next_x, next_y, next_d)] > next_cost):
                    visited[(next_x, next_y, next_d)] = next_cost
                    q.append((next_x, next_y, next_d, next_cost))

    return answer