from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        result = 0
        while 1:
            pop_cnt = 0
            
            for task, _ in counter.most_common(n + 1): #task실행
                pop_cnt += 1
                result += 1
                
                #실행한 결과 counter에 반영
                counter.subtract(task)
                #값이 0이하이면 아이템 목록에서 제거
                counter += Counter()
                
            #while문 종료조건 = 모든 task를 실행 했을 경우
            if not counter:
                return result
            
            #task를 n+1개 실행했으면 result는 그대로
            result += n - pop_cnt + 1