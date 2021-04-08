"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]

"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        basically any interval whose endtime is between the newInterval's start and end
        OR
        any interval whose starttime is between newInterval's start and end
        OR 
        if the existing interval completely overlaps the newInterval


        break the loop if start of the current interval is > newIntervalEnd

        newIntervalStart = min(interval's start time, newIntervalStart)
        newIntervalEnd = max(interval's endtime, newIntervalEnd)


        """
        # edge case
        if not intervals:
            return [newInterval]

        result = []
        [newStart, newEnd] = newInterval

        # adding this for the 3rd condition check below in the for loop
        intervals.append([float("inf"), float("inf")])

        for i in range(len(intervals)):
            # if we are looking at overlapping intervals with the newInterval
            # mash them up in one and keep updating the newStart and newEnd
            # so we check all the ways they could overlap
            newIntervalOverlapsEnd = newStart <= intervals[i][1] <= newEnd
            newIntervalOverlapsStart = newStart <= intervals[i][0] <= newEnd
            existingIntervalOverlaps = intervals[i][0] <= newStart <= newEnd <= intervals[i][1]

            # anything that comes before the newInterval
            # add it to the result directly
            if intervals[i][1] < newStart:
                result.append(intervals[i])

            # if overlap is seen then update the newStart and newEnd
            elif newIntervalOverlapsStart or newIntervalOverlapsEnd or existingIntervalOverlaps:
                newStart = min(intervals[i][0], newStart)
                newEnd = max(intervals[i][1], newEnd)

            # once we see an interval that is outside the range of newStart and newEnd
            # we can stop the looping, add the (newStart, newEnd), and the intervals beyond
            # the current position
            # I added a new interval [float("inf"), float("inf")] above, so this is always reached
            elif intervals[i][0] > newEnd:
                result.append([newStart, newEnd])
                result += intervals[i:]
                break

        # return everything but the last element which is the dummy I added
        return result[:len(result) - 1]
