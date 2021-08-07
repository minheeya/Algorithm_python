# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#l1, l2는 순서 그래로 앞에서 부터 계산하고 올림은 그 다음으로 올리면
#따로 역순을 구해 계산하지 않아도 됨.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        head = node = ListNode(0)
        carry = 0 #자리올림 수
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val 
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
                
            carry, val = divmod(sum + carry, 10)
            
            node.next = ListNode(val) #node의 다음에 연결
            node = node.next  #다음 노드를 가르킴
        
        return head.next  #head는 0, None 이기 때문에 그 다음 노드를 반환  