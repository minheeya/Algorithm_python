import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #(거리, 좌표)로 최소힙에 추가
        Q = []
        for x, y in points:
            heapq.heappush(Q, (x ** 2 + y ** 2, [x, y]))
        
        #거리가 가까운 순으로 k개를 pop()하여 result에 좌표만 추가
        result = []
        for _ in range(k):
            point = heapq.heappop(Q)
            result.append(point[1])
        
        return result