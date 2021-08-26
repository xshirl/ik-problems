def can_attend_all_meetings(intervals):
    intervals.sort(key=lambda x: x[0])
    
    i = 1
    while i < len(intervals):
        if intervals[i-1][1] > intervals[i][0]:
            return 0
        i += 1
    return 1
            