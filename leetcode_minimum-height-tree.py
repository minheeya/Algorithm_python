from collections import defaultdict
class Solution:
    #최소 높이를 가지는 root return
    #최소 높이를 가지는 root는 가운데에 위치해있음
    #리프노드를 제거하다 보면 가운데에 있는 노드만 남게됨
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        #그래프 구현
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
            
        #첫번째 리프노드 구하기 -> 리프노드는 그래프에서 길이가 1인 리스트를 값으로 갖음
        leaves = []
        for key in graph:
            if len(graph[key]) == 1:
                leaves.append(key)
        
        while n > 2:  #가운데 노드만 남을때까지 리프노드 제거
            n -= len(leaves)
            next_leaves = []
            for node in leaves:
                #리프노드와 연결되어 있는 노드와 연결상태 제거
                neighbor = graph[node].pop() 
                graph[neighbor].remove(node)  
                
                if len(graph[neighbor]) == 1:
                    next_leaves.append(neighbor)
            leaves = next_leaves
            
        return leaves