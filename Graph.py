#연결 된 배열들을 클래스 함수에 넣으면 Adjacency List로 Graph를 return 해주는 Graph class구현
#우선 Graph는 방향이 없는것으로 구현
#DFS, BFS 를 Graph class의 함수로 구현

from collections import deque

class Graph:
    def __init__(self, v_num):
        self.graph = {}    #그래프를 딕셔너리 형태로 선언
        for v in range(v_num):
            self.graph[v] = []  #총 노드 개수만큼 키 만들어줌

    def printGraph(self):
        return self.graph
    
    def addEdge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def dfs_stack(self, start_v = 0):
        visited = []
        stack = [start_v]
        while stack:
            v = stack.pop()   #v 꺼내서
            if v not in visited:
                visited.append(v)
                stack.extend(self.graph[v])
        return visited

    def dfs_recursion(self, v = 0, visited = []):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.dfs_recursion(i, visited)
        return visited

    def bfs(self, start_v = 0):  
        visited = []
        queue = deque([start_v])
        while queue:
            v = queue.popleft()
            if v not in visited:
                visited.append(v)
                queue.extend(self.graph[v]) 
        return visited

g = Graph(9)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(5, 6)
g.addEdge(5, 7)
g.addEdge(6, 8)
print('그래프 : ', g.printGraph())
print('stack을 이용한 dfs : ', g.dfs_stack())
print('recursion을 이용한 dfs : ', g.dfs_recursion())
print('queue를 이용한 bfs : ',g.bfs())