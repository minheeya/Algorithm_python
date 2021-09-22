T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    r = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)   #두 중점 사이 거리

    if r == 0 and r1 == r2:  #일치
        print(-1)
    elif r == r1 + r2 or r == abs(r1 - r2):  #한점에서 만날경우 (내접, 외접)
        print(1)
    elif r > r1 + r2 or r < abs(r1 - r2):   #만나지 않을 경우
        print(0)
    else:    #두 점에서 만날경우
        print(2)