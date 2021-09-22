N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

cnt = float('inf')
for i_start in range(N - 7):
    for j_start in range(M - 7):
        cnt_B, cnt_W = 0, 0
        for i in range(i_start, i_start + 8):
            for j in range(j_start, j_start + 8):
                if (i + j) % 2:  #행과 열의 합이 홀수 일 경우
                    if board[i][j] == 'B':
                        cnt_B += 1
                    else:
                        cnt_W += 1
                else:    #행과 열의 합이 짝수 일 경우
                    if board[i][j] == 'B':
                        cnt_W += 1
                    else:
                        cnt_B += 1
        cnt = min(cnt, min(cnt_B, cnt_W))

print(cnt)
