f = dict()
f[0] = (1, 0)  #0출력 횟수, 1출력 횟수
f[1] = (0, 1)
def fibonacci(n):
    if n not in f:
        f[n] = (fibonacci(n - 1)[0] + fibonacci(n - 2)[0], fibonacci(n - 1)[1] + fibonacci(n - 2)[1])
    return f[n]

for _ in range(int(input())):
    zero, one = fibonacci(int(input()))
    print(zero, one)