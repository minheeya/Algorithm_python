import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
ops = list(map(int, sys.stdin.readline().split()))  #+, - , x, %

max_value = float('-inf')
min_value = float('inf')

def dfs(depth, result):
    global max_value, min_value

    if depth == N:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return
    
    for i in range(4):
        if ops[i]:
            ops[i] -= 1
            if i == 0:
                dfs(depth + 1, result + nums[depth])
            elif i == 1:
                dfs(depth + 1, result - nums[depth])
            elif i == 2:
                dfs(depth + 1, result * nums[depth])
            elif i == 3:
                dfs(depth + 1, int(result / nums[depth]))
            ops[i] += 1;  #원상복구

dfs(1, nums[0])
print(max_value)
print(min_value)