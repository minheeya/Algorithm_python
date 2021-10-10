def solution(n, lost, reserve):
    #중복 제거하는 전처리
    reserve, lost = set(reserve) - set(lost), set(lost) - set(reserve) 
    
    for student in reserve:
        if student - 1 in lost:
            lost.remove(student - 1)
        elif student + 1 in lost:
            lost.remove(student + 1)
        
    return n - len(lost)