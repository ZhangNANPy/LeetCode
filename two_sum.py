# -*- coding: utf-8 -*-
"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        将遍历过的值哈希，并尝试返回一个和当前遍历值相匹配的哈希表中的值。O(n)
        """
        numd = {}
        for i in range(len(nums)):
            try:
                return [numd[target-nums[i]], i]
            except KeyError:
                numd[nums[i]] = i
