# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, sum = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val < low:
                    stack.append(node.right)
                elif node.val > high:
                    stack.append(node.left)
                else: #low <= node.val <= high:
                    sum += node.val
                    stack.append(node.right)
                    stack.append(node.left)
                
        return sum