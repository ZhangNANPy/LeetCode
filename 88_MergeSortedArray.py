# -*- coding: utf-8 -*-
# @File  : 88_MergeSortedArray.py
# @Author: ZRN
# @Date  : 2019/5/18
"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
"""


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        temp = nums1[:m]
        temp = temp + nums2
        temp.sort()
        for i in range(len(temp)):
            nums1[i] = temp[i]
