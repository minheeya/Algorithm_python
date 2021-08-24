# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        distance, prev = float('inf'), float('-inf')
        stack, node = [], root
        while stack or node:
            while node:   #왼쪽 노드를 stack에 추가
                stack.append(node)
                node = node.left
            
            node = stack.pop()   
            distance = min(distance, node.val - prev)
            prev = node.val
            
            node = node.right  #오른쪽 노드로 이동
         
        return distance
            