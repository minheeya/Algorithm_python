from collections import defaultdict
import heapq
def solution(n, edge):
    answer = 0
    
    #그래프를 인접리스트로 표현
    graph = defaultdict(list)
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    #q = [(거리, 노드), ...] / path = { 노드: 1부터 노드까지의 최단거리, ... }
    q, path = [(0, 1)], {}
    while 1:
        dist, node = heapq.heappop(q)
        if node not in path: #아직 최단거리를 구하지 않았을 경우
            path[node] = dist #최단거리 추가
            for v in graph[node]:
                heapq.heappush(q, (dist + 1, v))
        if len(path) == n: #모든 노드에 대하여 최단경로를 구하면
            dist_list = list(path.values()) 
            return dist_list.count(dist_list[-1]) #최대값의 개수 count하여 반환