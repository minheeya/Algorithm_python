import bisect
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        #하나의 리스트를 순회하면서 다른 하나는 이진검색으로 찾음
        child_i = 0
        for i in s:
            index = bisect.bisect_right(g, i) #g에 i값을 추가 가능한 가장 오른쪽 위치
            if child_i < index:
                child_i += 1
        
        return child_i
            