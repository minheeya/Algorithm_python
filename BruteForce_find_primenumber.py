from itertools import permutations

#소수 판별 함수
def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True if num > 1 else False
    
def solution(numbers):
    prime_nums = set()
    for n in range(1, len(numbers) + 1):
        for tp in permutations(numbers, n):
            if is_prime(int(''.join(tp))):
                prime_nums.add(int(''.join(tp)))
    
    return len(prime_nums)