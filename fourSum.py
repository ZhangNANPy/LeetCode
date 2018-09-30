# -*- coding: utf-8 -*-
"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if target < sum(nums[i:i + 4]) or target > sum(nums[-4:]):
                break
            if target > nums[i] + sum(nums[-3:]):
                continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target or nums[i] + sum(nums[-3:]) < target:
                    break
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    fsum = nums[i] + nums[j] + nums[l] + nums[r]
                    if fsum > target:
                        r -= 1
                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1
                    elif fsum < target:
                        l += 1
                        while l < r and nums[i] == nums[i - 1]:
                            l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[i] == nums[i - 1]:
                            l += 1
                        r -= 1
                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
