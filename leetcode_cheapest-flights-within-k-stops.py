from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w)) #(도착 정점, 비용)
        
        visited = {}      #방문 한 노드 기록 -> {노드 : 남아있는 경유지의 개수}
        Q = [(0, src, k + 1)]  #(비용, 출발 정점, 남아있는 경유지의 개수)
        while Q:
            price, node, cnt = heapq.heappop(Q)
            
            #도착지에 도착했을 경우
            if node == dst:
                return price
            
            if cnt and (node not in visited or visited[node] < cnt):
                #방문하지 않은 노드면 값 추가 / 
                #방문했던 노드지만 남아있는 경유지의 개수가 더 많으면 새로 값을 변경
                visited[node] = cnt
                for v, w in graph[node]:
                    heapq.heappush(Q,(price + w, v, cnt - 1))
        
        return -1