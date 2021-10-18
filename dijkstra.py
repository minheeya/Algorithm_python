#다익스트라 구현 ex로 네트워크 딜레이타임

from collections import defaultdict
import heapq

def networkDelayTime(times, N, K):  #time: 연결 시간, N: 노드개수, K: 출발지   #u,v,w 출발, 도착, 시간
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {}
    Q = [(0, K)] #(시간, 노드)
    while Q:
        time, node = heapq.heappop(Q)   #걸리는시간, 노드
        if node not in dist:  
            dist[node] = time  #도착지 : ㅅㅣ간
            for v, w in graph[node]:
                heapq.heappush(Q, (time+w, v))

    if len(dist) != N:
        return -1
    
    return max(dist.values()) 

print(networkDelayTime([[2,1,1], [2,3,1], [3,4,1]], 4, 2))
print(networkDelayTime([[3,1,5], [3,2,2], [2,1,2], [3,4,1], [4,5,1], [5,6,1], [6,7,1], [7,8,1], [8,1,1]], 8, 3))
