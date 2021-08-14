class Solution(object):
    def removeDuplicateLetters(self, s):
        #s중 사전순으로 가장 먼저 있는 알파벳부터 시작
        for c in sorted(set(s)):
            suffix = s[s.index(c):]  #현재 알파벳부터 끝까지 = 접미어
            #현재 알파벳부터 끝까지의 문자열이 가지고 있는 알파벳과 전체s가 가지고 있는 알파벳이 같음
            #=> 현재 위치 앞의 알파벳들은 중복이고, 제거한다.
            if set(s) == set(suffix):
                #접미어에 현재 알파벳을 제거하고 매개변수로 전달 (중복제거 위해)
                return c + self.removeDuplicateLetters(suffix.replace(c,''))
        
        return ''
    #그냥 return하면 None이 반환되어 + 연산 수행하지 못함
    #=> Typeerror 발생!