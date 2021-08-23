# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = 0
    #중위순회 (오른쪽-부모-왼쪽)
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)   #오른쪽 자식노드
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)    #왼쪽 자식노드
            
        return root
        