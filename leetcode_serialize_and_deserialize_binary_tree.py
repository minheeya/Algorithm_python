# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Codec:
    #직렬화 -> 논리적인 구조로 되어있는 이진트리를 배열로(물리적인 구조로) return
    def serialize(self, root):
        nodes = [None]   #인덱스 계산 쉽게 하기 위해 0은 NULL값으로 채우고 인덱스1부터 시작
        q = deque([root])
        while q:
            node = q.popleft()
            
            if node:  #node가 None이 아닐경우
                nodes.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:    #None일 경우
                nodes.append(None)
                
        return nodes
    
    #역직렬화 -> 배열로 되어있는 이진트리를 원래의 논리적인 구조로 return
    def deserialize(self, data):
        
        if data == [None, None]:   #예외처리
            return None
        
        root = TreeNode(data[1])
        q, idx = deque([root]), 2    #처음시작 인덱스 1 , 다음 노드는 인덱스 2
        while q:
            node = q.popleft()
            
            if data[idx] != None:  #왼쪽 노드 값 존재할 경우
                node.left = TreeNode(data[idx])
                q.append(node.left)
            idx += 1   #왼쪽 다음 오른쪽노드로 이동
            
            if data[idx] != None:  #오른쪽 노드 존재할 경우
                node.right = TreeNode(data[idx])
                q.append(node.right)  #오른쪽 다음 왼쪽 노드로 이동
            idx += 1
            
        return root