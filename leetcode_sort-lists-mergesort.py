# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTowList(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTowList(l1.next, l2)
        
        return l1 or l2 #둘 다 값이 있으면 l1, 둘 중 하나만 값 있으면 값이 있는것 return
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        #중앙지점 찾아서 분할
        #연결리스트 이기 때문에 런너기법을 활용하여 연결리스트 분할
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None #연결을 끊어 분할되게 함
        #단일 아이템이 될 때까지 계속하여 분할
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.mergeTowList(l1, l2)