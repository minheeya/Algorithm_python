from collections import defaultdict

def solution(begin, target, words):
    
    words.append(begin) #그래프 만들기 위해 시작점 begin단어 추가
    n = len(words) 
    
    #그래프 생성 (한개의 알파벳만 다를경우 =  인접)
    #주의할 점: 다른 알파벳의 위치가 같아야함 ( (ex) 'min'과 'mnk'는 인접하지X)
    graph = defaultdict(list)
    for i in range(n-1):
        before = words[i]
        for j in range(i+1, n):
            after = words[j]
            df_cnt = 0
            for bf, af in zip(words[i], words[j]):
                if bf != af:
                    df_cnt += 1
                    if df_cnt > 1:
                        break
            if df_cnt == 1:
                graph[before].append(after)
                graph[after].append(before)
    
    #BFS
    visited = []
    q = [(begin, 0)]  #[(node, 거리)]
    while q:
        node, cnt = q.pop()
        if node == target: 
            return cnt
        if node not in visited:
            visited.append(node)
            for v in graph[node]:
                q.append((v, cnt + 1))
    return 0