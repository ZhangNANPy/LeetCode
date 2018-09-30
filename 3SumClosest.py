# -*- coding: utf-8 -*-
"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return []
        i = 0
        nums.sort()
        last_num = nums[0] - 1
        res = nums[0] + nums[1] + nums[2]
        while i < len(nums) - 2:
            if nums[i] == last_num:
                i += 1
                continue
            begin = i + 1
            end = len(nums) - 1
            while begin < end:
                tsum = nums[begin] + nums[end] + nums[i]
                if abs(tsum - target) < abs(res - target):
                    res = tsum
                if tsum > target:
                    temp = nums[end]
                    while end >= begin and nums[end] == temp:
                        end -= 1
                elif tsum < target:
                    temp = nums[begin]
                    while begin < end and nums[begin] == temp:
                        begin += 1
                else:
                    return tsum
            last_num = nums[i]
            i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1,2,1,-4], 1))
