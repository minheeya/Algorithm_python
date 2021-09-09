class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(size): #size=확인 할 바이트 개수
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10: #앞 비트 2개가 10이어야 함
                    return False
            return True

        start = 0  #data의 0인덱스가 시작점
        while start < len(data):
            first = data[start]
            if (first >> 3) == 0b11110 and check(3): #4바이트로 표현
                start += 4
            elif (first >> 4) == 0b1110 and check(2): #3바이트로 표현
                start += 3
            elif (first >> 5) == 0b110 and check(1): #2바이트로 표현
                start += 2
            elif (first >> 7) == 0b0: #1바이트로 표현
                start += 1
            else:
                return False
        return True