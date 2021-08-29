# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #step1) 연결리스트를 파이썬의 리스트로 변경
        lst, p = [], head #리스트, 포인터 변수
        while p:
            lst.append(p.val)
            p = p.next
        
        #step2) 파이썬 sort() 메서드 사용하여 리스트 정렬
        lst.sort()
        
        #step3) 파이썬 리스트를 연결리스트로 변경
        p = head #포인터 변수
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head