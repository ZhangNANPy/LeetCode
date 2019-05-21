# -*- coding: utf-8 -*-
# @File  : 78_Subsets.py
# @Author: ZRN
# @Date  : 2019/5/15
"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。
"""


class Solution:
    def subsets(self, nums):
        res = []
        for i in range(2 ** (len(nums))):
            s = bin(i)[2:]
            cur = []
            for j in range(len(s)):
                cur += [nums[j]] if s[~j] == '1' else []
            res.append(cur)
        return res
