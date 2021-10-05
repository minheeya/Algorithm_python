from collections import deque
from itertools import permutations

def solution(expression):
    answer = 0

    op = []
    nums = []
    num = ''

    #연산자와 숫자 나눠서 저장
    for s in expression:
        if s == '+':
            nums.append(int(num))
            num = ''
            op.append('+')
        elif s == '-':
            nums.append(int(num))
            num = ''
            op.append('-')
        elif s == '*':
            nums.append(int(num))
            num = ''
            op.append('*')
        else:
            num += s
    nums.append(int(num))

    #우선순위 정하고 각 경우일때 상금 구하기
    
    for case in permutations(set(op)):
        op_temp = deque(op)
        nums_temp = deque(nums)
        for c in case:
            while c in op_temp:
                idx = op_temp.index(c)
                nums_temp[idx] = cal(c, nums_temp[idx], nums_temp[idx+1])
                delIdx(nums_temp, idx + 1)
                delIdx(op_temp, idx)
        answer = max(answer, abs(nums_temp[0]))

    return answer

def cal(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    else:
        return num1 * num2

def delIdx(dq, idx):
    temp = deque()
    for i in range(idx):
        temp.appendleft(dq.popleft())
    dq.popleft()
    dq.extendleft(temp)
    return dq