def solution(n, computers):
    network_cnt = n #네트워크 개수의 초기값

    for start_v in range(n): 
        #dfs
        visited = [] #하나의 brunch에 연결 되어 있는 node
        stack  = [start_v]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                for i in range(n):
                    if node != i and computers[node][i]:
                        stack.append(i)
                        computers[node][i] = 0 #이미 지나온 길은 0으로 만듬
                        computers[i][node] = 0
                        
        if len(visited) != 1: #시작노드 말고 다른 노드를 방문한 경우
            #한 네트워크로 연결 된 컴퓨터 개수를 빼고 1을 더함
            network_cnt += (-len(visited) + 1) 
            
    return network_cnt