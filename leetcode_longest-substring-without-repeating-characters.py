class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        used = {}
        start = max_len = 0
        for i, char in enumerate(s):
            if char in used and start <= used[char]: #중복 된 문자열일 경우
                start = used[char] + 1
            else:
                max_len = max(max_len, i - start + 1)
            
            #문자char의 위치를 최근위치 i로 갱신
            used[char] = i

        return max_len