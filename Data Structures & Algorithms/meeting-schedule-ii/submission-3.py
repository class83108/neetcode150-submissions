"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) < 1:
            return 0
        
        if len(intervals) == 1:
            return 1

        points = []
        for interval in intervals:
            points.append([interval.start, "S"])
            points.append([interval.end, "E"])

        points.sort(key=lambda x: (x[0], x[1]))
        
        max_room = 0
        curr_room = 0

        for point, point_type in points:
            if point_type == "E":
                curr_room -= 1
            
            else:
                curr_room += 1

            max_room = max(max_room, curr_room)

        return max_room

        