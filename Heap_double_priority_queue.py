import heapq

def solution(operations):
    
    q = []
    for operation in operations:
        op, num = operation.split()
        if op == 'I':
            heapq.heappush(q, int(num))
        elif q and op == 'D':  #삭제 연산
            if num == '-1':  #최솟값 삭제
                heapq.heappop(q)
            else:      #최댓값 삭제
                q.sort()
                q.pop()
    
    if not q:  #q가 비어있을 경우
        return [0, 0]
    
    q.sort()   #q가 비어있지 않을 경우
    
    return [q[-1], q[0]]