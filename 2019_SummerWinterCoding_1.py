def solution(w,h):
    answer = 0
    
    if w == 1 or h ==1 :
        return 0
    elif w == h:
        return w * h - h
    else:
        for x in range(1, w+1):
            y = (-h/w)*x + h
            answer += int(y)
        return answer*2