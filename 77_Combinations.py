# -*- coding: utf-8 -*-
# @File  : 77_Combinations.py
# @Author: ZRN
# @Date  : 2019/5/15
"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
"""


class Solution:
    def combine(self, n: int, k: int):
        res = []
        for s in self.combine_str(n, k):
            cur = []
            for i, c in enumerate(s):
                if c == '1':
                    cur.append(i + 1)
            res.append(cur)
        return res

    def combine_str(self, n: int, k: int) -> list:
        if n == 0:
            return ['']
        if k == 0:
            return ['0' * n]
        if n == k:
            return ['1' * n]
        res = ['1' + s for s in self.combine_str(n - 1, k - 1)] + ['0' + s for s in self.combine_str(n - 1, k)]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
