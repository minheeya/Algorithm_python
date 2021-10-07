def solution(citations):
    
    N = len(citations)
    citations.sort()
    
    h = 0
    for idx, val in enumerate(citations):
        if val > N - idx: #N - idx = 자신 포함 val이상인 논문 개수
            h = max(h, N - idx)
            break
        h = val
    
    return h