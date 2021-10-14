def solution(routes):
    routes.sort(reverse = True)
    answer = 0
    while routes:
        answer += 1
        start, end = routes.pop()
        while routes and routes[-1][0] <= end:
            s, e = routes.pop()
            start, end = max(start, s), min(end, e)

    return answer