def solution(number, k):
    stack = []
    for i, num in enumerate(number):
        if not k:
            stack.extend(number[i:])
            return ''.join(stack)
        
        while stack and k and num > stack[-1]:
            stack.pop()
            k -= 1
        stack.append(num)
        
    return ''.join(stack[:len(stack) - k])