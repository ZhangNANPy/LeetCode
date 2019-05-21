# -*- coding: utf-8 -*-
# @File  : 80_RemoveDuplicatesfromSortedArrayII.py
# @Author: ZRN
# @Date  : 2019/5/16
"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        i = 1
        last_letter = nums[0]
        count = 1
        while i < len(nums):
            if nums[i] == last_letter and count == 2:
                del nums[i]
            elif nums[i] == last_letter and count < 2:
                count += 1
                i += 1
            elif nums[i] != last_letter:
                last_letter = nums[i]
                count = 1
                i += 1
        return len(nums)
