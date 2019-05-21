# -*- coding: utf-8 -*-
# @File  : 73_SetMatrixZeroes.py
# @Author: ZRN
# @Date  : 2019/5/13
"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
"""


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        columns = set()
        for i in range(len(matrix)):
            flag = False
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    flag = True
                    columns.add(j)
            if flag:
                matrix[i] = [0] * len(matrix[i])
        for c in columns:
            for i in range(len(matrix)):
                matrix[i][c] = 0
