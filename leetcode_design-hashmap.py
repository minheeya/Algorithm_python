class ListNode: #연결리스트 노드 클래스
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        
from collections import defaultdict
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        
        #해당키를 해싱한 인덱스가 존재하지 않을경우
        if self.table[idx].value is None:
            self.table[idx] = ListNode(key, value)
            return
            
        #존재할 경우 key값이 같으면 정보를 업데이트 하고, 키 값이 없으면 새로 추가해줌
        p = self.table[idx] #첫번째 인덱스 가리킴
        while p:
            if p.key == key: #정보 업데이트
                p.value = value
                return
            if p.next is None: #마지막 인덱스일 경우
                break
            p = p.next #p다음으로 이동
        p.next = ListNode(key, value) #새로운 노드 추가
        

    def get(self, key: int) -> int:
        idx = key % self.size
        
        #해당키를 해싱한 인덱스가 존재하지 않을경우
        if self.table[idx].value is None:
            return -1
        
        p = self.table[idx]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
        

    def remove(self, key: int) -> None:
        idx = key % self.size
        
        #해당키를 해싱한 인덱스가 존재하지 않을경우
        if self.table[idx].value is None:
            return
        
        #첫번째 노드가 삭제할 노드일 경우
        p = self.table[idx]
        if p.key == key:
            #노드가 유일할 경우 ListNode()로 값 변경
            #뒤에 연결 된 노드가 있을경우 다음노드(p.next)로 값 변경
            self.table[idx] = ListNode() if p.next == None else p.next
            return
        
        #첫번째 노드가 삭제할 노드가 아닐경우
        prev = p 
        while p:
            if p.key == key:
                prev.next = p.next
                return 
            prev, p = p, p.next
        