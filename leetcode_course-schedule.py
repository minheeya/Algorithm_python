from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for after, before in prerequisites:
            graph[after].append(before)
        
        #dfs
        visited, traced = [], [] #순환구조 판별 완료한 노드, 이전에 방문했던 노드
        def dfs(node):
            if node in traced: #이전에 방문한 노드일경우
                return False
            
            if node in visited:
                return True
            
            traced.append(node)
            for v in graph[node]: 
                if not dfs(v): #자식노드가 이전에 방문한 노드일경우
                    return False
            traced.pop()  #탐색 종료 후 순환 노드 삭제
            visited.append(node)  #순환구조 판별 완료
            
            return True
        
        #각 노드에서 출발하는 모든경우를 따지는 이유
        #-> 그래프가 끊어져 있는 경우에서 cyclic 판별하기 위해!
        for node in list(graph): #dict를 list로 변경하면 key만 list의 요소로 들어감
            if not dfs(node):  #dfs에서 False return될 경우
                return False

        return True