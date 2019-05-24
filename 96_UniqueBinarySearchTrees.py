# -*- coding: utf-8 -*-
# @File  : 96_UniqueBinarySearchTrees.py
# @Author: ZRN
# @Date  : 2019/5/24
"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
"""


class Solution:
    def numTrees(self, n: int) -> int:
        trees = [1, 1]
        for i in range(2, n + 1):
            total = 0
            for j in range(i):
                total += trees[j] * trees[i - j - 1]
            trees.append(total)
        return trees[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(3))
