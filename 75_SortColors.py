# -*- coding: utf-8 -*-
# @File  : 75_SortColors.py
# @Author: ZRN
# @Date  : 2019/5/13
"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。
"""


class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        boundary_0 = 0
        boundary_2 = len(nums) - 1
        i = 0
        while i <= boundary_2:
            if nums[i] == 0:
                nums[i], nums[boundary_0] = nums[boundary_0], nums[i]
                boundary_0 += 1
                i = max(i, boundary_0)
            elif nums[i] == 2:
                nums[i], nums[boundary_2] = nums[boundary_2], nums[i]
                boundary_2 -= 1
            else:
                i += 1
