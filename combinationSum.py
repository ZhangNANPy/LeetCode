# -*- coding: utf-8 -*-
# @File  : combinationSum.py
# @Author: ZRN
# @Date  : 2018/10/10
"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

* 所有数字（包括 target）都是正整数。
* 解集不能包含重复的组合。
"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        while not candidates and candidates[-1] > target:
            del candidates[-1]
        if not candidates:
            return []
        return self.combination_sum_it(candidates, target)

    def combination_sum_it(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[List[int]]
        """
        if len(nums) == 1:
            if target % nums[0] == 0:
                return [nums * (target // nums[0])]
            else:
                return []
        res = []
        for i in range(0, target // nums[0] + 1):
            temp_re = self.combination_sum_it(nums[1:], target - nums[0] * i)
            for re in temp_re:
                res.append([nums[0]] * i + re)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
