def solution(numbers, hand):
    answer = ''

    L_i, L_j = 3, 0   #왼쪽 엄지 위치
    R_i, R_j = 3, 2   #오른쪽 엄지 위치

    for num in numbers:
        i, j = place(num)

        if j == 0:
            L_i, L_j = i, j #1,4,7 일때 왼손 이동
            answer += 'L'
        elif j == 2:
            R_i, R_j = i, j #3,6,9 일때 오른손 이동
            answer += 'R'
        else:
            R_d = abs(R_i - i) + abs(R_j - j)
            L_d = abs(L_i - i) + abs(L_j - j)

            if R_d < L_d:   #오른손이 더 가까울 경우
                R_i, R_j = i, j 
                answer += 'R'
            elif L_d < R_d:  #왼손이 더 가까울 경우
                L_i, L_j = i, j 
                answer += 'L'
            else:  #똑같을 경우
                if hand == 'right':
                    R_i, R_j = i, j 
                    answer += 'R'
                else:
                    L_i, L_j = i, j 
                    answer += 'L'

    return answer

def place(number):

    # i 위치
    if number == 0:
        i = 3
    elif number < 4:
        i = 0
    elif number < 7:
        i = 1
    else:
        i = 2

    # j 위치
    if number % 3 == 1:
        j = 0
    elif number % 3 == 2 or number == 0:
        j = 1
    else:
        j = 2
    
    return (i,j)