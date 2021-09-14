class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums2.sort()
        for i in range(len(nums1)):
            left, right = 0, len(nums2) -1
            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] == nums1[i] and nums2[mid] not in res:
                    res.append(nums2[mid])
                elif nums2[mid] < nums1[i]:
                    left = mid + 1
                else:
                    right = mid - 1
        return res