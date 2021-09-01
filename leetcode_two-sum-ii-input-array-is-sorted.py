import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            expected = target - n
            idx = bisect.bisect_left(numbers, expected, i + 1)
            if idx < len(numbers) and numbers[idx] == expected:
                return i + 1, idx + 1