class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0]*len(temperatures)
        
        stack = []
        for i, temp in enumerate(temperatures):
            #현재온도보다 낮은 온도가 stack에 없을때까지 
            while stack and temperatures[stack[-1]] < temp:
                last = stack.pop()
                answer[last] = i - last  #일수 차이 (=인덱스 차이)
            stack.append(i)
        
        return answer