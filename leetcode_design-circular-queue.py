class MyCircularQueue(object):

    def __init__(self, k):
        self.maxlen = k
        self.q = [None] * k
        self.p1 = 0  #맨 앞 요소 가르키는 포인터
        self.p2 = 0  #맨 뒤 요소 그 다음 가르키는
        

    def enQueue(self, value): #추가 연산은 p2가 이동
        if self.q[self.p2] == None:
            self.q[self.p2] = value #값 추가
            self.p2 = (self.p2 + 1) % self.maxlen #p2를 다음으로 이동 
            # 포인터 % maxlen 하는 이유 => 마지막 다음은 0 인덱스로 돌아와야하기 때문
            return True
        else: #가득 차 있어 추가 불가능함
            False
        
    def deQueue(self): #삭제 연산은 p1이 이동
        if self.q[self.p1] == None: #비어있으므로 삭제 불가
            return False
        else:
            self.q[self.p1] = None #삭제
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self): #가장 맨 앞 요소 return
        #큐가 비어있을 경우 -1 return
        return -1 if self.q[self.p1] == None else self.q[self.p1]
        

    def Rear(self):  #가장 마지막 요소 return
        #큐가 비어있을 경우 -1 return
        return -1 if self.q[self.p2 - 1] == None else self.q[self.p2 - 1]
        #q는 파이썬의 리스트로 구성되어 있음 
        #=>마지막 값을 -1인덱스로 표현 
        #=> q[p2 - 1]는 항상 p2가 가르키는 위치의 전 값 가르킴
        #ex) p2 = 0일 때, 전 값의 위치는 4(마지막 인덱스) / 0 - 1 = -1(마지막 인덱스)
    
    def isEmpty(self):
        if self.p1 == self.p2 and self.q[self.p1] == None:
            return True
        else:
            return False
        

    def isFull(self):
        if self.p1 == self.p2 and self.q[self.p1] != None:
            return True
        else:
            return False
        
