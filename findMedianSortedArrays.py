# -*- coding: utf-8 -*-
"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
你可以假设 nums1 和 nums2 不同时为空。
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        target = (len(nums1) + len(nums2)) // 2
        median_index = self.get_index(nums1, nums2, target)
        if (len(nums1) + len(nums2)) % 2 == 1:
            return [nums1, nums2][median_index[0]][median_index[1]]
        else:
            median_index1 = self.get_index(nums1, nums2, target - 1)
            return ([nums1, nums2][median_index[0]][median_index[1]] +
                    [nums1, nums2][median_index1[0]][median_index1[1]]) / 2

    def get_index(self, nums1, nums2, target):
        """
        :param nums1: list
        :param nums2: list
        :param target: int
        :return: list[int, int] 指明target指出的索引位于哪个数组的哪个索引
        """
        if not nums1:
            return [1, target]
        elif not nums2:
            return [0, target]
        half_index = len(nums1) // 2
        added_index = self.get_item_index(nums2, nums1[half_index])
        if half_index + added_index > target:
            return self.get_index(nums1[:half_index], nums2[:added_index + 1], target)
        elif half_index + added_index < target:
            result = self.get_index(nums1[half_index + 1:], nums2[added_index:],
                                    target - added_index - half_index - 1)
            if result[0] == 0:
                result[1] = result[1] + half_index + 1
            elif result[0] == 1:
                result[1] = result[1] + added_index
            return result
        elif half_index + added_index == target:
            return [0, half_index]

    def get_item_index(self, l, target):
        """
        :param l: list
        :param target: int
        :return: int  保持列表有序，给定target的插入索引
        """
        if l[0] > target:
            return 0
        elif l[-1] <= target:
            return len(l)
        half = len(l) // 2
        if l[half] <= target < l[half + 1]:
            return half + 1
        elif l[half] > target:
            return self.get_item_index(l[:half], target)
        elif l[half + 1] <= target:
            return half + 1 + self.get_item_index(l[half + 1:], target)


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 5, 6], [2, 3, 4, 7, 8, 9, 10]))
