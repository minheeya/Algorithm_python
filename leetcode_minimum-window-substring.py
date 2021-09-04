from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        missing = len(t)  #찾아야 할 문자 개수
        
        left, start, end = 0, 0, 0
        for right, char in enumerate(s):
            missing -= need[char] > 0
            need[char] -= 1  #char가 존재하지 않으면 0-1 = -1 (음수)
            
            if missing == 0: #모든 문자 다 찾았을 경우
                #left가 필요한 문자를 가르키도록 이동
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                #더 작은 범위를 start, end에 저장
                if not end or right - left < end - start:
                    start, end = left, right
                
                need[s[left]] += 1
                missing += 1
                left += 1
        
        if start == 0 and end == 0 and (t != s[0]): #예외처리
            return ""
                
        return s[start: end + 1]