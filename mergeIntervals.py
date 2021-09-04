class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        i = 1
        j = 0

        while i < len(intervals):
            if intervals[j][1] >= intervals[i][0]:
                intervals[j][0] = min(intervals[j][0], intervals[i][0])
                intervals[j][1] = max(intervals[j][1], intervals[i][1])
                del intervals[i]
            else:
                j += 1
                i += 1
        return intervals
