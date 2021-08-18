class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer, prev_e = [], []
        def dfs(elements):
            #재귀함수 종료조건
            if not elements:
                answer.append(prev_e[:])
                return
            
            for e in elements:
                #elements을 prev_e와 next_e로 나눔
                next_e = elements[:]  #파이썬은 객체를 참조함에 유의
                next_e.remove(e)  #현재값을 제외한 요소들을 next_e에
                prev_e.append(e)  #현재값을 prev_e에 위치하게 함
                dfs(next_e)
                prev_e.pop()   #재귀함수 종료휴 prev_e = []로 만들기 위해 하나 씩 pop
                
        dfs(nums)
        
        return answer