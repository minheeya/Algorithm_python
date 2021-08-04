#최소 3개의 구간이 존재해야 물이 고일 수 있는 환경이 만들어짐
#현재 높이가 이전 높이보다 클 경우
#3개의 구간을 잡고, 해당구간으로 만들어 지는 물의 부피를 더해준다
#-> top = stack.pop() 하면 3개의 구간의 인덱스는 stack[-1], top, i(현재)
#-> 물의 부피는 가로*세로

class Solution(object):
    def trap(self, height):
        volume, stack = 0, []
        for i in range(len(height)):
            #stack에 있는 인덱스들의 높이가 현재의 높이보다 작을 경우 계속 반복
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop() #중간 구간
                
                #stack이 비어있는 경우(=3개의 구간을 만들 수 없는 경우) 빠져나감
                if not stack:
                    break
                    
                #처음 구간 stack[-1] / 중간구간 top / 마지막구간 i
                width = i - stack[-1] - 1 #가로
                length = min(height[i], height[stack[-1]]) - height[top] #높이
                
                volume += width * length
                
            stack.append(i)

        return volume
            