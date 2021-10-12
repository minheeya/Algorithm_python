def solution(name):
    counts = [min(ord(char)-ord('A'), ord('Z')-ord(char)+1) for char in name]
    
    answer, idx = 0, 0
    while 1:
        answer += counts[idx]
        counts[idx] = 0
        
        if sum(counts) == 0:
            break
            
        left, right = 1, 1 #기본이동 횟수
        while counts[idx - left] == 0:
            left += 1
        while counts[idx + right] == 0:
            right += 1
        answer += left if left < right else right
        idx += -left if left < right else right
        
    return answer