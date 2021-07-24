#섞은 횟수 return
#heapq모듈로 최소힙 구현

import heapq

def solution(scoville, K):
    answer = 0 
    scoville.sort() #최소힙에서는 가장 작은 값이 인덱스0에 위치해야한다.
    while 1:
        first = heapq.heappop(scoville) #가장 안 매운 음식
        if first < K:
            if not scoville: #마지막 음식이 k보다 작을 경우
                return -1
            second = heapq.heappop(scoville) #두번째로 안 매운 음식
            heapq.heappush(scoville, first + second*2)
            answer += 1 #섞은 횟수 카운트
        else:
            return answer
