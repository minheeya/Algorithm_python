# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #재귀함수
        def check(node):
            #리프노드(None)도착
            if not node:
                return 0
            
            left = check(node.left)
            right = check(node.right)
            
            #두 서브트리간의 높이차가 1 이상일 경우 -1 return
            #left, right 둘 중 하나라도 -1이면 계속 -1을 return
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1  #둘 중 큰것 + 1 = 상태값
        
        return check(root) != -1