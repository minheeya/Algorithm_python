from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        
        strs = [] #카운트 할 문자만 모아놓을 리스트
        for s in re.sub(r'[^\w]', ' ', paragraph).lower().split():
            if s not in banned: #금지 된 단어랑 다를 경우
                strs.append(s)  

        return Counter(strs).most_common(1)[0][0]