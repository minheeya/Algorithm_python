class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #양쪽 다 정렬하여 투 포인터로 풀이
        nums1.sort()
        nums2.sort()
        
        result = set()
        i, j = 0, 0 #각각 nums1,nums2의 포인터
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return result
        