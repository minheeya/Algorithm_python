def solution(routes):
    answer = 0
    last_camera = float('-inf')
    routes.sort(key=lambda x: x[1]) #진출 순서대로 정렬

    for s, f in routes:
        if s > last_camera: #겹치는 구간 없는 경우
            answer += 1
            last_camera = f

    return answer