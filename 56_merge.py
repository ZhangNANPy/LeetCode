# -*- coding: utf-8 -*-
# @File  : 56_merge.py
# @Author: ZRN
# @Date  : 2019/4/22
"""
给出一个区间的集合，请合并所有重叠的区间
示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda interval: interval[0])
        i = 1
        while i < len(intervals):
            if intervals[i - 1][1] >= intervals[i][0]:
                intervals[i - 1][1] = max(intervals[i][1], intervals[i - 1][1])
                del intervals[i]
            else:
                i += 1
        return intervals


if __name__ == '__main__':
    t = [[1, 3], [0, 6], [8, 10], [15, 18]]
    s = Solution()
    for i in s.merge(t):
        print(i[0], i[1])
