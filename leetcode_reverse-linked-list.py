# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        
        node, prev = head, None
        while node:
            #next 변수에 node.next할당
            #node.next에 현재까지 완성 된 역순연결리스트 할당
            next, node.next = node.next, prev
            prev = node   #node까지 추가해서 완성 된 역순연결리스트 재할당
            #아직 역순연결리스트가 되지 않은 부분(next)를 node에 할당하여 None이 될때까지 반복
            node = next   
        
        return prev
