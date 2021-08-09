# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        root = start = ListNode(None)
        root.next = head
        
        #start를 역순으로바꿔야할 첫 시작 위치의 바로 앞을 가리키도록 이동
        for _ in range(left - 1):
            start = start.next
        end = start.next  #역순으로 바꿨을때 가장 마지막에 올 노드
     
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        
        return root.next