class Solution(object):
    def oddEvenList(self, head):
        
        #예외처리 (노드의 개수 n의 최솟값은 0 => 다음 로직을 처리하려면 적어도 한개의 노드가 필요함)
        if not head:
            return head
        
        odd = head #홀수번째 노드
        even_head = even = head.next #짝수번째 노드
        
        while even and even.next:
            #각각 다음 홀수, 짝수 번째 노드와 연결하고 이동
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next  
        
        odd.next = even_head  #홀수번째 노드의 마지막을 짝수번째 노드의 처음과 연결
        
        return head