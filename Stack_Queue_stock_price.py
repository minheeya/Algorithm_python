def solution(prices):
    answer = [n for n in range(len(prices)-1, -1, -1)]  #reverse사용해도 됨
    stack = []
    for i, val in enumerate(prices):
        #가격이 떨어지면 그 가격보다 큰 가격이 없을때까지 pop
        while stack and val < prices[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
        
    return answer