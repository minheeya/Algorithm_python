class Solution(object):
    def swapPairs(self, head):
        
        if head and head.next:
            p = head.next  #두번째 노드를 지정
            head.next = self.swapPairs(p.next) #첫번째 노드가 다음 다음을 가르키도록 하는데, 재귀함수로 백트래킹되면서 연결됨
            p.next = head  #두번째 노드가 첫번째 노드를 가르키도록 함
            
            return p  
        
        return head