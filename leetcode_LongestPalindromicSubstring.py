class Solution(object):
    def longestPalindrome(self, s):
        #팰린드롬 일 경우 계속하여 왼쪽, 오른쪽으로 확장해나아가는 함수
        def expand(left, right): #투 포인터 left, right
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1 #왼쪽으로 확장
                right += 1 #오른쪽으로 확장
            return s[left + 1:right]
        
        #길이가1 이거나 s전체가 팰린드롬 일 경우 s를 그대로 return
        if len(s) < 2 or s == s[::-1]:
            return s
        
        longest = '' #가장 긴 팰린드롬
        #길이가 짝수인 팰린드롬(초기 길이 2), 홀수인 팰린드롬(초기길이3)으로 시작
        for i in range(len(s)-1):  
            longest = max(longest, expand(i, i + 1), expand(i, i + 2), key = len)
        
        return longest

#max도 key속성 이용하여 기준 정할 수 있음