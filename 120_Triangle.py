# -*- coding: utf-8 -*-
# @File  : 120_Triangle.py
# @Author: ZRN
# @Date  : 2019/6/21
"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
"""


class Solution:
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]
        sums = [0]
        for row in triangle:
            temp = [row[0] + sums[0]]
            for i in range(1, len(row) - 1):
                temp.append(min(sums[i - 1], sums[i]) + row[i])
            temp.append(row[-1] + sums[-1])
            sums = temp
        return min(sums)


if __name__ == '__main__':
    s = Solution()
    t = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(s.minimumTotal(t))
