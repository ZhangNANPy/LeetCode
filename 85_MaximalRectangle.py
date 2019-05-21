# -*- coding: utf-8 -*-
# @File  : 85_MaximalRectangle.py
# @Author: ZRN
# @Date  : 2019/5/17
"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
"""


class Solution:
    def maximalRectangle(self, matrix) -> int:  # ot
        if not matrix:
            return 0

        res = [0] * len(matrix[0])
        for i in range(len(matrix)):
            hs = []
            for j in range(len(matrix[i])):
                if matrix[i][j] == '0':
                    hs.append(0)
                else:
                    count = 0
                    h = i
                    while h >= 0 and matrix[h][j] == '1':
                        h -= 1
                        count += 1
                    hs.append(count)
            res.append(self.largestRectangleArea(hs))
        return max(res)

    def largestRectangleArea(self, heights):
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
    m = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    print(s.maximalRectangle(m))
