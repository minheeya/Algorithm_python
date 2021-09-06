class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        #계산 함수
        def cal(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
                
            return results
        
        if expression.isdigit():
            return [int(expression)]
        
        #연산자를 기준으로 분할
        results = []
        for i, char in enumerate(expression):
            if char in '+-*': #char이 연산자 일 경우 분할
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                
                results.extend(cal(left, right, char))
            
        return results