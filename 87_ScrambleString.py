# -*- coding: utf-8 -*-
# @File  : 87_ScrambleString.py
# @Author: ZRN
# @Date  : 2019/5/18
"""
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。
我们将 "rgeat” 称作 "great" 的一个扰乱字符串。
我们将 "rgtae” 称作 "great" 的一个扰乱字符串。
给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。
"""

from collections import defaultdict
from copy import deepcopy


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in range(len(s1)):
            d1[s1[i]] += 1
            d2[s2[i]] += 1
        if d1 == d2:
            return self.itScramble(s1, s2, d1, d2)
        return False

    def itScramble(self, s1, s2, d1, d2) -> bool:
        if not s1 or s1 == s2:
            return True
        if len(s1) < 4 and d1 == d2:  # 支持任意序
            return True
        d1left = defaultdict(int)
        d1right = deepcopy(d1)
        d2left = defaultdict(int)
        d2right = deepcopy(d2)
        red2left = deepcopy(d2)
        red2right = defaultdict(int)
        flag = False
        for i in range(len(s1) - 1):
            if flag:
                return True
            d1left[s1[i]] += 1
            d1right[s1[i]] -= 1
            d2left[s2[i]] += 1
            d2right[s2[i]] -= 1
            red2left[s2[~i]] -= 1
            red2right[s2[~i]] += 1
            if d1left == d2left and d1right == d2right:
                flag = flag or self.itScramble(s1[:i + 1], s2[:i + 1], d1left, d2left) \
                               and self.itScramble(s1[i + 1:], s2[i + 1:], d1right, d2right)
            if flag:
                return True
            if d1left == red2right and d1right == red2left:
                flag = flag or self.itScramble(s1[:i + 1], s2[~i:], d1left, red2right) \
                               and self.itScramble(s1[i + 1:], s2[:~i], d1right, red2left)
        return flag


if __name__ == '__main__':
    s = Solution()
    print(s.isScramble("hobobyk", "hbyokbo"))
