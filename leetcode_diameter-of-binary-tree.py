# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    distance = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            
            if not node:
                return -1
            
            #왼쪽, 오른쪽 각 리프노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            #경로의 가장 긴 길이
            self.distance = max(self.distance, left + right + 2)
            
            return max(left, right) + 1

        dfs(root)
        return self.distance