# 2020카카오인턴십_동굴탐험
# 문제를 보려면 다음 링크로 들어가세요 https://programmers.co.kr/learn/courses/30/lessons/67260

from collections import defaultdict

def solution(n, path, order):
    answer = True
    
    #part1 => 초기값 설정
    graph = defaultdict(list)   # 방의 연결상태를 딕셔너리 형태의 그래프로 표현
    before = defaultdict(int)   # ex) before = {y:x} => y를 방문하기 전에 x를 방문해야함 
    after = defaultdict(int)    # ex) after = {x:y} => x를 방문하고나서 y를 방문해야함
    
    for i in range(n-1):  
        v1, v2 = path[i][0], path[i][1]
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for i in range(len(order)):
        if order[i][1] == 0:   #0은 가장 처음에 방문해야 됨
            return False
        before[order[i][1]] = order[i][0]
    
    #part2 => DFS적용
    visited = [False]*n #각 n개의 방 방문여부 => False:방문X / True:방문O
    stack = [0] #0부터 시작
    while stack:
        node = stack.pop()
        #현재 노드 전 방문해야 하는 노드를 방문하지 않았을 경우
        if node in before and not visited[before[node]]:
            after[before[node]] = node
            continue #아래 코드들 실행하지 않고 바로 다음 반복으로 넘어감
        
        visited[node] = True
        for nd in graph[node]:
            if not visited[nd]: #방문하지 않은 노드일경우 stack에 추가
                stack.append(nd)
        
        #해당 노드를 방문하고 그 다음에 방문할 노드가 있으면 stak에 추가
        if node in after:
            stack.append(after[node])
        
    if False in visited:   #방문하지 않은곳이 한 곳이라도 있을경우
        answer = False
    
    return answer


