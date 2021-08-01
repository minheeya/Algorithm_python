class Solution(object):
    def reorderLogFiles(self, logs):
        letter, digit= [], []
        for log in logs:
            if log.split()[1].isdigit():  #0인덱스는 식별자
                digit.append(log)
            else:
                letter.append(log)
        
        #digit-logs는 순서를 유지
        #letter-logs는 컨텐츠를 사전순으로 정렬. 
        #만약 컨텐츠가 같다면, 식별자를 사전순으로 정렬
        letter.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        
        #letter-logs가 digit-logs보다 앞에 존재해야 함
        return letter + digit