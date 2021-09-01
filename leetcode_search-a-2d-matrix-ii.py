class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1 #matrix[row][col] 행, 렬
        while row < len(matrix) and col >= 0:
            if matrix[row][col] < target: #target보다 작을 때
                row += 1
            elif matrix[row][col] > target: #target보다 클 때
                col -= 1
            else: #target과 같을때
                return True
        return False