import heapq
def solution(jobs):
    #제일 먼저 요청 된 작업이 맨 뒤에 오도록 내림차순 정렬
    jobs.sort(reverse = True)
    
    N = len(jobs)   #총 작업의 개수
    cmplete_N = N   #완료 해야 할 작업의 개수
    
    start, end = -1, 0  #작업 시작 시간, 작업 완료 시간
    hq, sum_t = [], 0   #heap자료구조 , 소요시간 총 합
    while cmplete_N: #전체 반복문은 완료된 작업이 N개일때 종료 
        #현재 시점에서 처리 할 수 있는 작업들을 heap에 추가하는 과정
        while jobs:
            if jobs[-1][0] <= end:
                rq_time, size = jobs.pop()  #요청시간, 소요시간
                heapq.heappush(hq, (size, rq_time))
            else:
                break
        #heap에 담긴 작업 수행 => 가장 작은 소요시간을 가진 작업 먼저 수행
        if hq:
            size, rq_time = heapq.heappop(hq)  #소요시간, 요청시간
            start = end           #다음 직업 시작 시간 = 이전 작업 완료 시간
            end = start + size  #다음 작업 완료 시간 = 작업 시작 시간 + 소요시간
            sum_t += end - rq_time  #작업 끝나는 시간 - 작업 요청 시간
            cmplete_N -= 1                 #작업을 완료할 때마다 1씩 감소
        else:
            end += 1              #종료시간을 1씩 증가시키며 새로운 일이 들어오길 기다림
            
    return sum_t // N