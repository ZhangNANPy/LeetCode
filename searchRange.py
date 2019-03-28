# -*- coding: utf-8 -*-
# @File  : searchRange.py
# @Author: ZRN
# @Date  : 2018/10/8
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        l = 0
        r = len(nums) - 1
        res = [-1, -1]
        while l < r and (res[0] == -1 or res[1] == -1):
            mid = (l + r) // 2
            if nums[l] == target:
                res[0] = l
            else:
                right_boundary = mid
                while nums[right_boundary] >= target and l < right_boundary :
                    right_boundary = (l + right_boundary) // 2
                l = right_boundary if right_boundary > l else min(l + 1, len(nums) - 1)
            if nums[r] == target:
                res[1] = r
            else:
                left_boundary = mid
                while nums[left_boundary] <= target and r > left_boundary:
                    left_boundary = (r + left_boundary) // 2 + 1
                r = left_boundary if left_boundary < r else max(r - 1, 0)
        if l == r and nums[l] == target:
            res = [l, l]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 9], 6))
