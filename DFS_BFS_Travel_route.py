from collections import defaultdict
def solution(tickets):
    #티켓 내림차순 정렬 
    tickets.sort(reverse = True)
    
    #그래프 인접리스트 형태로 표현
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    
    route = [] #경로를 담을 리스트 (마지막부터 처음까지 거꾸로 담김)
    
    #DFS(recursion구현)
    def dfs(start):
        while graph[start]:
            dfs(graph[start].pop())
        route.append(start)
    
    dfs('ICN') #'ICN에서 출발'
    
    return route[::-1]