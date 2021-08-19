from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #그래프 구현
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))  #(정점, 걸린시간)
        
        #bfs
        visited = {}  #방문한 노드
        Q = [(0, k)]  #우선순위 큐 (시간, 정점)
        while Q:
            time, node = heapq.heappop(Q)
            
            if node not in visited:
                visited[node] = time
                for v, w in graph[node]:
                    heapq.heappush(Q, (time + w, v))  #(시간, 정점)추가
            
            if len(visited) == n:  #모든 노드 신호 받음
                return max(list(visited.values()))
        
        return -1 #모든 노드 신호 받지 못함