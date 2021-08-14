from collections import deque
class MyStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, x):
        #가장 최근에 넣은 데이터가 가장 앞에 있을 수 있도록(큐에서 가장 먼저 pop될 수 있도록) 위치시킴
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()
        

    def top(self):
        #스택에서 top은 가장 최근에 넣은 데이터 = pop하면 나올 수 있도록 0에 위치시킴
        return self.q[0]  
        

    def empty(self):
        return len(self.q) == 0