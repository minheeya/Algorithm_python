def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    visited = {costs[0][0]}  #방문 한 섬
    answer = 0
    while len(visited) != n:
        for island1, island2, cost in costs:
            if len({island1, island2} & visited) == 1:
                visited.update([island1, island2])
                answer += cost
                break #노드가 추가 되었으므로 len(visited) != n 조건 확인
                
    return answer