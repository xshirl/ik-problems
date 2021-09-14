class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        index = -1
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == mid:
                index = mid
                right = mid - 1
            elif arr[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1
        return index