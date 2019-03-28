# -*- coding: utf-8 -*-
# @File  : maxSubArray.py
# @Author: ZRN
# @Date  : 2018/10/31
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        max_sum = nums[0]
        while i < len(nums) and nums[i] <= 0:
            max_sum = max(max_sum, nums[i])
            i += 1
        cur_sum = 0
        while i < len(nums):
            if cur_sum + nums[i] <= 0:
                cur_sum = 0
            else:
                cur_sum += nums[i]
                max_sum = max(max_sum, cur_sum)
            i += 1
        return max_sum
