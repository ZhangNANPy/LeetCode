# -*- coding: utf-8 -*-
# @File  : spiralOrder.py
# @Author: ZRN
# @Date  : 2018/11/19
"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
"""


class Solution:
    def __init__(self):
        self.re = []

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return self.re
        if len(matrix) <= 1:
            self.re += matrix[0]
            return self.re
        if len(matrix[0]) == 1:
            for l in matrix:
                self.re += l
            return self.re

        self.re += matrix[0]
        for i in range(1, len(matrix) - 1):
            self.re.append(matrix[i][-1])
        matrix[-1].reverse()
        self.re += matrix[-1]
        for i in range(len(matrix) - 2, 0, -1):
            self.re.append(matrix[i][0])

        if len(matrix) <= 2:
            return self.re
        else:
            del matrix[0]
            del matrix[-1]

        if len(matrix[0]) <= 2:
            return self.re
        else:
            for l in matrix:
                del l[0]
                del l[-1]

        return self.spiralOrder(matrix)


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(s.spiralOrder(matrix))
