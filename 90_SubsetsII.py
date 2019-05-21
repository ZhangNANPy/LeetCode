# -*- coding: utf-8 -*-
# @File  : 90_SubsetsII.py
# @Author: ZRN
# @Date  : 2019/5/18
"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。
"""


class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [[], [nums[0]]]

        nums.sort()
        res = [[], [nums[0]]]
        left = 1
        right = 2
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                for j in range(left, right):
                    res.append(res[j] + [nums[i]])
                left = right
                right = len(res)
            else:
                left = len(res)
                for j in range(len(res)):
                    res.append(res[j] + [nums[i]])
                right = len(res)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([4, 1, 0]))
