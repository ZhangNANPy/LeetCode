# -*- coding: utf-8 -*-
# @File  : 57_InsertInterval.py
# @Author: ZRN
# @Date  : 2019/4/23
"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        flag = True
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                flag = False
                intervals.insert(i, newInterval)
                break
        if flag:
            intervals.append(newInterval)
        i = 1
        while i < len(intervals):
            if intervals[i - 1][1] >= intervals[i][0]:
                intervals[i - 1][1] = max(intervals[i][1], intervals[i - 1][1])
                del intervals[i]
            else:
                i += 1
        return intervals
