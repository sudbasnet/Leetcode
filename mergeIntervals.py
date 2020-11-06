"""Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""


class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        """
        1 -------- 6 8 -- 10
           3 --- 5
         2 -- 4
         
         we track the start and end of the most recently started meeting.
         if the next meeting starts after this end time, then we save the first and 
         the start and end variable not contains the time of the second intervals
         
         if we overlap we update the start and end values to min(start1, start2) --- to --- max(end1, end2)
        """
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort()
        mergedIntervals = []
        [start, end] = intervals[0]
        
        for i in range(1, len(intervals)): 
            if intervals[i][0] > end:
                mergedIntervals.append([start, end])
                [start, end] = intervals[i]
            elif intervals[i][0] <= end:
                end = max(end, intervals[i][1])
        return mergedIntervals + [[start, end]]
        
        