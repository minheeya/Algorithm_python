def solution(rows, columns, queries):
    answer = []
    
    board, num = dict(), 1
    for i in range(rows):   #board[(위치)] = 위치에 있는 숫자
        for j in range(columns):
            board[(i+1, j+1)] = num
            num += 1
            
    for x1, y1, x2, y2 in queries:
        start = (i, j) = (x1, y1) #첫 시작 위치
        min_num = board[start]  #최솟값 
        for n in [1, -1]:
            for cnt in range(y2-y1):
                j += n
                board[start], board[i, j] = board[i, j],  board[start]
                min_num = min(min_num, board[start])
            for cnt in range(x2-x1):
                i += n
                board[start], board[i, j] = board[i, j], board[start]
                min_num = min(min_num, board[start])
        answer.append(min_num)
    
    return answer