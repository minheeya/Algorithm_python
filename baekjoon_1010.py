def factorial(number, cnt):
    mul = 1
    for _ in range(cnt):
        mul *= number
        number -=1
        
    return mul

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(factorial(m, n) // factorial(n, n))