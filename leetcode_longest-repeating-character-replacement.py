from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        left = 0
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            
            max_char_n = counts.most_common(1)[0][1] #윈도우 내의 가장 많이 있는 문자 개수
            
            #윈도우 내의 전체 문자 개수(right-left) - 윈도우 내의 가장 많이 있는 문자 개수 
            #= 변경해야 할 문자 개수
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        
        return right - left