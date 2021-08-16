class MyCircularDeque(object):

    def __init__(self, k):
        self.maxlen, self.len = k, 0
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.right, self.tail.left = self.tail, self.head
        
    def _add(self, node, new):  #(추가할 노드의 위치 보다 하나 앞의 위치에 있는 노드, 추가할 노드)
        n = node.right  #node의 다음 node를 n으로 지정
        node.right = new
        n.left = new
        new.left, new.right = node, n
    
    def _del(self, node): #(삭제할 노드의 위치 보다 하나 앞의 위치에 있는 노드)
        n = node.right.right  #node의 다음 다음 위치에 있는 node를 n으로 지정
        node.right = n
        n.left = node
        
    def insertFront(self, value):
        if self.len == self.maxlen:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
        
    def insertLast(self, value):
        if self.len == self.maxlen:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True
        

    def deleteFront(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True
        

    def deleteLast(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True
        

    def getFront(self):
        return -1 if self.len == 0 else self.head.right.val
        

    def getRear(self):
        return -1 if self.len == 0 else self.tail.left.val
        

    def isEmpty(self):
        return self.len == 0
        

    def isFull(self):
        return self.len == self.maxlen