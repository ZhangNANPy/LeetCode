# -*- coding: utf-8 -*-
# @File  : 74_Search2DMatrix.py
# @Author: ZRN
# @Date  : 2019/5/13
"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。一拳超人漫画
每行的第一个整数大于前一行的最后一个整数。
"""


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        for i in range(len(matrix)):
            if not matrix[i]:
                del matrix[i]
        if not matrix:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        start = 0
        end = len(matrix) - 1
        while start <= end:
            row = (start + end) // 2
            if target < matrix[row][0]:
                end = row - 1
            elif target > matrix[row][-1]:
                start = row + 1
            else:
                break
        start = 0
        end = len(matrix[row]) - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[row][mid] < target:
                start = mid + 1
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [[1]]
    print(s.searchMatrix(matrix, 1))
