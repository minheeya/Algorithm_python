class Solution(object):
    def isPalindrome(self, s):
        
        s = s.lower() #s내의 문자 소문자로 변환
        #정규식을 사용하여 문자와 숫자 외 나머지 필터링(정규표현식 사용)
        s = re.sub('[^a-z0-9]','',s)
        
        return s == s[::-1] #슬라이싱