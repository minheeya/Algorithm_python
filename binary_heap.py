#최소 힙 구현
#루트노드에 최소값 존재
class BinaryHeap:
    def __init__(self):
        self.items = [None]  #인덱스 계산을 편하게 하기 위해 인덱스 1부터 시작하도록 0에는 None을 위치시킴
    
    def __len__(self):
        return len(self.items) - 1  #len함수 사용하면 len - 1을 return 하도록 내부기능동작 변경

    def _percolate_up(self):
        idx = len(self)
        parent = idx // 2  #부모 노드의 인덱스
        #상향식으로 현재 노드가 부모노드보다 클때까지 반복 & 부모 노드의 최소 위치는 1 (0에는 None있으므로)
        while parent and self.items[idx] < self.items[parent]:  
            self.items[idx], self.items[parent] = self.items[parent], self.items[idx]  #스왑
            idx = parent
            parent = idx // 2

    def insert(self, data):
        self.items.append(data)  #data를 맨 뒤에 삽입
        self._percolate_up()

    def _percolate_down(self, idx):
        left = idx * 2        #왼쪽 노드
        right = idx * 2 + 1   #오른쪽 노드
        smallest = idx        #부모 노드 (현재노드)

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != idx:  #값이 변경 되었을 경우
            self.items[smallest], self.items[idx] = self.items[idx], self.items[smallest]   #스왑
            return self._percolate_down(smallest)
            
    def extract(self):
        extracted = self.items[1]   #추출 할 값
        self.items[1] = self.items.pop()  #맨 마지막 값을 root노드로 이동
        #하향식으로 현재노드가 자식노드보다 작을때까지 재귀 호출
        self._percolate_down(1)  #루트노드 부터 시작
        return extracted

if __name__ == '__main__':
    binary_heap = BinaryHeap()
    #값 추가
    binary_heap.insert(16)
    print(binary_heap.items)
    binary_heap.insert(10)
    print(binary_heap.items)
    binary_heap.insert(14)
    print(binary_heap.items)
    binary_heap.insert(2)
    print(binary_heap.items)
    binary_heap.insert(4)
    print(binary_heap.items)
    binary_heap.insert(1)
    print(binary_heap.items)
    binary_heap.insert(8)
    print(binary_heap.items)
    binary_heap.insert(7)
    print(binary_heap.items)
    binary_heap.insert(9)
    print(binary_heap.items)
    binary_heap.insert(3)
    print(binary_heap.items)
    binary_heap.insert(3)
    print(binary_heap.items)

    #값 추출
    print(binary_heap.extract())
    print(binary_heap.items)
    print(binary_heap.extract())
    print(binary_heap.items)
    print(binary_heap.extract())
    print(binary_heap.items)
    print(binary_heap.extract())
    print(binary_heap.items)
    print(binary_heap.extract())
    print(binary_heap.items)