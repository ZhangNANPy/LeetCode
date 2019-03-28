# -*- coding: utf-8 -*-
# @File  : searchInsert.py
# @Author: ZRN
# @Date  : 2018/10/8
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = min(mid + 1, len(nums) - 1)
            elif nums[mid] > target:
                r = mid
            else:
                return mid
        (l, r) = (l, r) if nums[l] >= nums[r] else r, l
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 6))
