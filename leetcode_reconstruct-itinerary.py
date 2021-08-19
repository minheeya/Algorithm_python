from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        #그래프 구성
        #pop()하면 사전어휘순으로 나올 수 있도록 내림차순 정렬
        graph = defaultdict(list)
        for start, end in sorted(tickets, reverse = True):
            graph[start].append(end)
        
        #재귀dfs (백트래킹 하여 경로 역순으로 추가)
        route = []
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            route.append(start)
            
        dfs('JFK')
        #경로를 역순으로 추가했으므로 다시 역순으로 바꾸어 return
        return route[::-1]