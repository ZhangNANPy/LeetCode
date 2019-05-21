# -*- coding: utf-8 -*-
# @File  : 84_LargestRectangleInHistogram.py
# @Author: ZRN
# @Date  : 2019/5/16
"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
"""


class Solution:
    def largestRectangleArea1(self, heights) -> int:
        """
        :param heights:
        :return: int
        用小数分割递归求解，OT
        """
        if not heights:
            return 0
        minl = []
        minh = float('inf')
        for i in range(len(heights)):
            if heights[i] < minh:
                minh = heights[i]
                minl = [i]
            elif heights[i] == minh:
                minl.append(i)
        area_list = [minh * len(heights), self.largestRectangleArea(heights[:minl[0]]),
                     self.largestRectangleArea(heights[minl[-1] + 1:])]
        for i in range(len(minl) - 1):
            area_list.append(self.largestRectangleArea(heights[minl[i] + 1: minl[i + 1]]))
        return max(area_list)

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        利用栈构造升序序列，若下一个数是升序则进栈，否则开始退栈，直到出现小于等于当前数的元素。注意栈内是升序序列，
        这就找到了介于两个小数之间的一个序列，计算这个序列的面积，之后将当前数入栈，直到栈长度达到之前长度+1.
        """
        if not heights:
            return 0

        res = 0
        stack = []  # 记录升序序列节点的索引
        heights.append(-1)
        for i in range(len(heights)):
            current = heights[i]
            while len(stack) != 0 and current <= heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if len(stack) == 0 else i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    hs = [2, 1, 5, 6, 2, 3]
    print(s.largestRectangleArea(hs))
