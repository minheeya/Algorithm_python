class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #중첩함수
        def dfs(index, path):
            #재귀 종료 조건 -> 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                answer.append(path)
                return
            
            for char in num_dic[digits[index]]:
                dfs(index + 1, path + char)
                
        #예외처리-> input이 digits = ""일 경우
        if not digits:   #빈 문자열이면 if, while같은 문의 조건에서 거짓으로 간주
            return []
        
        num_dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        answer = []
        dfs(0, "")
        
        return answer