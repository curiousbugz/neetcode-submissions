"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        event = []
        rooms = 0
        max_rooms = 0
        for interval in intervals:
            event.append((interval.start, 1))
            event.append((interval.end, -1))
        for _, change in sorted(event):
            rooms += change
            max_rooms=max(max_rooms,rooms)
        return max_rooms
