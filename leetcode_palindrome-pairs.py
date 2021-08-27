from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.pelindrome_word_ids = []
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    @staticmethod
    def is_pelindrome(word): 
        #클래스 및 객체와 연관되어 있는 것은 메서드 
        #독립적으로 존재하는 것은 함수
        #해당 메서드를 독립적으로 존재하는 함수로 만들어주기위해 데코레이터  @staticmethod로 선언
        return word[::] == word[::-1]
        
    def insert(self, idx, word):  #문자를 역순으로 삽입
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_pelindrome(word[0:len(word) - i]):
                node.pelindrome_word_ids.append(idx)
            node = node.children[char]
        node.word_id = idx
    
    def search(self, idx, word):
        result = []
        node = self.root
        
        #3번째 판별로직
        while word:
            #탐색 중 word_id의 값이 있을 경우
            if node.word_id >= 0:
                if self.is_pelindrome(word): #뒤의 나머지 문자열이 팰린드롬인지 확인
                    result.append([idx, node.word_id])
            #탐색 중 찾는 문자가 없을 경우
            if word[0] not in node.children:
                return result
            node = node.children[word[0]]  #노드 이동
            word = word[1:]
            
        #1번째 판별로직
        if node.word_id >= 0 and node.word_id != idx:
            result.append([idx, node.word_id])
            
        #2번째 판별로직
        for pelindrome_id in node.pelindrome_word_ids:
            result.append([idx, pelindrome_id])
            
        return result
        
        
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        
        #트라이 구현 (값 삽입)
        for idx, word in enumerate(words):
            trie.insert(idx, word)
        
        results = []
        for idx, word in enumerate(words):
            results.extend(trie.search(idx, word))
            
        return results
            
        
        