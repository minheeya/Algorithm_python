# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)  #popleft사용하기 위해 deque사용
        
        def div(preorder, inorder):
            if inorder:
                #preorder에서 분할 지점 구하기
                idx = inorder.index(preorder.popleft())
            
                #inorder에서 분할 지점을 기준으로 분할
                node = TreeNode(inorder[idx])
                node.left = div(preorder, inorder[:idx])
                node.right = div(preorder, inorder[idx + 1:])
            
                return node
        
        return div(preorder, inorder)