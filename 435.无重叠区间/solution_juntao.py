class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        count = 1
        n = len(intervals)
        intervals.sort(key=lambda ls: ls[1])
        target = intervals[0][1]
        for i in range (1, n):
            if intervals[i][0] >= target:
                count += 1
                target = intervals[i][1]
        return n - count


