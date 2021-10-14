def get_p(connection, node):
    if connection[node] == node:
        return node
    return get_p(connection, connection[node])

def solution(n, costs):
    costs.sort(key = lambda x: x[2], reverse = True)
    connection = [i for i in range(n)]  #연결 정보
    edges = []

    while len(edges) != n - 1:
        i1, i2, cost = costs.pop()
        #부모 노드가 다를 경우 연결 가능
        if get_p(connection, i1) != get_p(connection, i2):
            #연결 정보 갱신
            connection[get_p(connection, i1)] = i2
            edges.append(cost)

    return sum(edges)