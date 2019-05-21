# -*- coding: utf-8 -*-
# @File  : 81_SearchinRotatedSortedArrayII.py
# @Author: ZRN
# @Date  : 2019/5/16
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
"""


class Solution:
    def search(self, nums, target: int) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return target == nums[0]
        if len(nums) == 2:
            return target == nums[0] or target == nums[1]
        mid = len(nums) // 2
        if nums[0] < nums[mid]:
            if nums[0] <= target <= nums[mid]:
                return self.search(nums[0:mid + 1], target)
            else:
                return self.search(nums[mid + 1:], target)
        elif nums[0] == nums[mid]:
            return self.search(nums[0:mid + 1], target) or self.search(nums[mid + 1:], target)
        else:
            if nums[mid + 1] <= target <= nums[-1]:
                return self.search(nums[mid + 1:], target)
            else:
                return self.search(nums[0:mid + 1], target)


if __name__ == '__main__':
    s = Solution()
    print(s.search([1, 1, 1, 3, 1], 3))
