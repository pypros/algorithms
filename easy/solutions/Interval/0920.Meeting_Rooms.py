"""
https://www.lintcode.com/problem/920/

920 · Meeting Rooms
Given an array of meeting time intervals consisting of start and end 
times [(s1,e1),(s2,e2),...] (si < ei), determine if a person could attend all meetings.


0 ≤ intervals.length ≤ 10^4

intervals[i].length == 2

0 ≤ start(i) < end(i) ≤ 10^6

[(0,8), (8,10)] is not conflict at 8

Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict
Example2

Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 

"""

from dataclasses import dataclass
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

@dataclass
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i : i.start)
        for i in range(1, len(intervals)):
            i1 = intervals[i -1]
            i2 = intervals[i] 
            if i1.end > i2.start:
                return False
        return True
        # for i, interval in enumerate(intervals):
        #     start, _ = interval
        #     if i > 0 and start < intervals[i - 1][1]:
        #         return False
        # return True


import unittest


class SolutionTestCase(unittest.TestCase):
    solution = Solution()

    def test_example_1_leetcode(self):
        self.assertEqual(self.solution.can_attend_meetings([
            Interval(0,30),
            Interval(5,10),
            Interval(15,20),
        ]), False)

    def test_example_2_leetcode(self):
        self.assertEqual(self.solution.can_attend_meetings([
            Interval(5,8),
            Interval(9,15),
        ]), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)
