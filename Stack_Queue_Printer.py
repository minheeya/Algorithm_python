#큐 자료구조 사용 (FIFO)
#문서의 중요도 배열 priorities / 내 문서 위치 location
#내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return

from collections import deque
def solution(priorities, location):
    
    cnt = 0
    q = deque(list(enumerate(priorities)))
    while q:
        max_p = max([tp[1] for tp in q])
        if q[0][1] < max_p:
            q.append(q.popleft())
        else:
            document = q.popleft()
            cnt += 1
            if document[0] == location:
                return cnt