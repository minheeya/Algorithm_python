from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    #삽입
    def insert(self, word: str) -> None:
        node = self.root  #처음 위치
        for char in word:
            node = node.children[char]  #node를 다음 문자로 이동
        node.word = True  #단어가 완성되면 마지막 문자 노드에서 True로 표시
    
    #해당 단어가 존재하는지 여부 판별
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]   #node를 다음 문자로 이동
        return node.word
        
    #해당 문자열로 시작하는 단어가 있는지 여부 판별
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]   #node를 다음 문자로 이동
        return True