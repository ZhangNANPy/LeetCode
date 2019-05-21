# -*- coding: utf-8 -*-
# @File  : 59_SpiralMatrix2.py
# @Author: ZRN
# @Date  : 2019/4/29
"""
给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
"""


class Solution:
    def generateMatrix(self, n):
        m = [[0] * n for i in range(n)]
        center = n // 2
        num = 1
        for i in range(center):
            steps = n - i * 2 - 1
            for j in range(steps):
                m[i][i + j] = num
                num += 1
            for j in range(steps):
                m[i + j][i + steps] = num
                num += 1
            for j in range(steps):
                m[i + steps][i + steps - j] = num
                num += 1
            for j in range(steps):
                m[i + steps - j][i] = num
                num += 1

        if n % 2 == 1:
            m[center][center] = num
        return m


if __name__ == '__main__':
    s = Solution()
    m = s.generateMatrix(1)
    for i in m:
        print(i)
