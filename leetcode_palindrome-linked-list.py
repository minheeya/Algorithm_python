# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution(object):
    def isPalindrome(self, head):
        
        rev = None
        fast = slow = head
        while fast and fast.next: #fast가 끝까지 갈때까지
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        #홀수개의 node를 가지고 있으면 fast != None
        #짝수개의 node를 가지고 있으면 fast = None
        if fast:  #홀수개의 node를 가지고 있을 경우
            slow = slow.next #slow를 이동시켜 중간값은 비교하지 않도록 한다.
        
        #팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return not rev