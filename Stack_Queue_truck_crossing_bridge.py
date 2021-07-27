#트럭이 다리를 건너는데까지 걸리는 시간 = bridge_length
from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights) #큐 자료구조 사용
    trucks_on_bridge = deque([0] * bridge_length) #다리 위 트럭 list
    sec, sum_on_bridge = 0, 0 #시간, 다리 위 트럭 무게 합
    while trucks_on_bridge:
        sec += 1
        sum_on_bridge -= trucks_on_bridge.popleft()
        
        if truck_weights:
            if sum_on_bridge + truck_weights[0] <= weight:
                sum_on_bridge += truck_weights[0]
                trucks_on_bridge.append(truck_weights.popleft())
            else: 
                trucks_on_bridge.append(0)
    return sec