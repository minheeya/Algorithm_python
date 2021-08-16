# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        root = result = ListNode(None)
        
        #우선순위 큐 사용 / (값, 인덱스(몇 번째 리스트인지), 연결리스트) / 인덱스(몇 번째 리스트인지)
        #중복을 막기 위해 인덱스 사용 => 중복이면 error 나기 때문에
        Q = []
        for i, list in enumerate(lists):
            if list:
                heapq.heappush(Q, (list.val, i, list))
        
        while Q:
            node = heapq.heappop(Q)
            idx = node[1]
            result.next = node[2]
            
            result = result.next #result이동
            if result.next:
                heapq.heappush(Q, (result.next.val, idx, result.next))
        
        return root.next