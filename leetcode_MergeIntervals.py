class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() #시작점 순으로 정렬
        
        merged = []
        for part in intervals:
            if merged and part[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], part[1])
            else:
                merged += [part]
                
        return merged