# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = root = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                #head가 들어갈 위치를 찾을때까지 cur이동
                cur = cur.next 
            
            cur.next, head.next, head= head, cur.next, head.next
            
            #조건을 걸어 cur의 위치를 초기화 (최적화)
            if head and cur.next.val > head.val:
                #cur위치 초기화
                cur = root
        
        return root.next