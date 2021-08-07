# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        
        # not l1 => l1이 None 일때 스왚(마지막 노드의 next는 None 이므로)
        # l2 and l1.val > l2.val 
        #=> l2가 존재해야 l2.val이 존재하기 때문에 l2가 존재하는 부분 추가확인
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        
        if l1: #l1이 None이 아닐 경우 
            l1.next = self.mergeTwoLists(l1.next, l2)
        
        return l1   #l1이 None이 되면 재귀 끝. return 시작하고 백트래킹되면서 엮임