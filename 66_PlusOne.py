# -*- coding: utf-8 -*-
# @File  : 66_PlusOne.py
# @Author: ZRN
# @Date  : 2019/5/1
"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


class Solution:
    def plusOne(self, digits):
        return [int(i) for i in str(int("".join([str(j) for j in digits])) + 1)]


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 2, 3]))
