def solution(brown, yellow):
    answer = []
    
    #yellow부분 가로 x, 세로 y
    y = 1
    while y <= yellow:
        if yellow % y == 0:
            x = yellow // y
            if 2 * (x + y) + 4 == brown:
                return [x + 2, y + 2]
        y += 1
