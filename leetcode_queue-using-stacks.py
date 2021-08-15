class MyQueue(object):

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)
        
    def pop(self):
        self.peek()
        return self.output.pop()
        
    #output의 가장 마지막 인덱스에 pop할 데이터 위치시킴
    #output이 비어있다면 다시 갱신
    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        
    def empty(self):
        return self.input == [] and self.output == []