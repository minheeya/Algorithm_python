import heapq
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        hq = []
        #키가 최대인 사람 먼저 추출할 수 있도록 최대 힙 구성
        for person in people:
            heapq.heappush(hq, (-person[0], person[1]))
        
        #키가 최대인 사람 먼저 추출
        answer = []
        while hq:
            person = heapq.heappop(hq)
            #이미 자신보다 큰 사람들은 배치 완료 됨
            #따라서 앞에 줄서 있는 사람 중 자신의 키 이상인 사람들의 수 = 추가 할 index
            answer.insert(person[1], [-person[0], person[1]]) 
        
        return answer