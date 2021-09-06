class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #닶이 존재하지 않는 경우
        if sum(gas) < sum(cost):
            return -1
        
        #여기서부턴 무조건 답이 1개 존재
        #출발점이 안 되는 지점 판별
        start, fuel = 0, 0
        for i in range(len(gas)):
            if fuel + gas[i] < cost[i]: #이동 할 연료 모자를 경우
                #해당 지점이 출발점이 안 되는 지점으로 판별하면
                #앞에 있는 모든 지점들도 출발점이 될 수 없음
                start = i + 1 #start를 다음으로 이동
                fuel = 0 #연료 초기화
            else:
                fuel += gas[i] - cost[i]
        
        return start