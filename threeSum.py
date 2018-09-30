# -*- coding: utf-8 -*-
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = []
        i = 0
        nums.sort()
        last_num = nums[0] - 1
        while i < len(nums) and nums[i] < 1:
            if nums[i] == last_num:
                i += 1
                continue
            begin = i + 1
            end = len(nums) - 1
            while begin < end:
                if nums[begin] + nums[end] + nums[i] > 0:
                    temp = nums[end]
                    while end >= begin and nums[end] == temp:
                        end -= 1
                elif nums[begin] + nums[end] + nums[i] < 0:
                    temp = nums[begin]
                    while begin < end and nums[begin] == temp:
                        begin += 1
                else:
                    res.append([nums[i], nums[begin], nums[end]]) # 这个顺序无关
                    temp = nums[begin]
                    while begin < end and nums[begin] == temp:
                        begin += 1
            last_num = nums[i]
            i += 1
        return res

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = {}
        for ele in nums:
            dic[ele] = dic.get(ele, 0) + 1
        neg = sorted(filter(lambda x: x < 0, dic))
        pos = sorted(filter(lambda x: x >= 0, dic))
        if 0 in dic and dic[0] > 2:
            res = [[0, 0, 0]]
        else:
            res = []
        for ele1 in neg:
            for ele2 in pos:
                tar = -(ele1 + ele2)
                if tar in dic:
                    if tar in (ele1, ele2) and dic[tar] > 1:
                        res.append([ele1, tar, ele2])
                    elif tar < ele1 or tar > ele2:  # 这里写法不是唯一的，要保证两个子句所指示的区间相互不覆盖。在此条件下，找寻tar的方向总是一样的，可以保证唯一性。
                        res.append([ele1, tar, ele2])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
