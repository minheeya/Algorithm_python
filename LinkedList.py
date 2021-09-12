#단순연결리스트

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def __str__(self):
        list_str=''
        
        node = self.head
        while node.next != None:
            list_str += str(node.data) + '->'
            node = node.next
        list_str += str(node.data)
        
        return list_str
    
    def listSize(self):
        return self.size

    def isEmpty(self):
        if self.size != 0:
            return False
        else:
            return True

    def selectNode(self, idx):
        if idx >= self.size:
            print('IndexError')
            return
        else:
            node = self.head
            for cnt in range(idx):
                node = node.next
        return node

    def insertFirst(self, data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            self.head = Node(data, self.head)
        self.size += 1
        
    def insertMiddle(self, data, idx):
        if self.isEmpty():
            if idx != 0:
                print('IndexError')
            else:
                self.head = Node(data)
                self.size += 1
            return
        if idx == 0:
            self.head = Node(data, self.head)
        else:
            node = self.selectNode(idx-1)
            node.next = Node(data, node.next)
        self.size += 1
            
    def insertLast(self, data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            self.selectNode(self.size-1).next = Node(data)
            #node = self.head
            #while node.next != None:
            #    node = node.next
            #node.next = Node(data)
        self.size += 1
        
    def deleteNode(self, idx):
        if self.isEmpty():
            print('Underflow: Empty Linked List Error')
            return
        elif idx >= self.size:
            print('Overflow: IndexError')
            return
        elif idx == 0:
            node = self.head
            self.head = node.next
            del(node)
        else:
            node = self.selectNode(idx-1)
            del_node = self.selectNode(idx)
            node.next = del_node.next
            del(del_node)
        self.size -= 1

if __name__ == '__main__':
    mylist = SLinkedList()
    mylist.insertLast('A')
    print(mylist)
    mylist.insertLast('B')
    print(mylist)
    mylist.insertLast('C')
    print(mylist)
    mylist.insertMiddle('D', 1)
    print(mylist)
    mylist.insertFirst('E')
    print(mylist)
    print(mylist.listSize())
    mylist.deleteNode(0)
    print(mylist)
    mylist.deleteNode(3)
    print(mylist)    
    mylist.deleteNode(0)
    print(mylist)
    mylist.insertFirst('A')
    print(mylist)