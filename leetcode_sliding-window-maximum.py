from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        dq, start = deque(), 0
        for i, n in enumerate(nums):
            #dq[0]은 최대값의 인덱스
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            
            if i < k - 1:  #dq초기값 생성하기 위해 0,1,..,k-2은 위에만 반복
                continue
            
            while 1:
                if dq[0] >= start:  #최대값이 범위 안에 존재할 경우
                    answer.append(nums[dq[0]])
                    break
                else:
                    dq.popleft()
            start += 1  #시작위치 + 1
            
        return answer