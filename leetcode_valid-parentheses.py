class Solution(object):
    def isValid(self, s):
        table = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for c in s:
            if c not in table:
                stack.append(c)
            #stack이 비어있거나 짝이 안맞을경우
            elif not stack or stack.pop() != table[c]:
                return False
        #input = '[' 인경우 예외처리
        return len(stack) == 0  