# -*- coding: utf-8 -*-
# @File  : 97_InterleavingString.py
# @Author: ZRN
# @Date  : 2019/5/24
"""
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        from collections import defaultdict
        d12 = defaultdict(int)
        d3 = defaultdict(int)
        for c in s1:
            d12[c] += 1
        for c in s2:
            d12[c] += 1
        for c in s3:
            d3[c] += 1
        if d3 != d12:
            return False
        self.res = dict()
        return self.reInterleave(s1, s2, s3)

    def reInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (s1, s2, s3) in self.res:
            return self.res[(s1, s2, s3)]
        if not s1 or not s2:
            self.res[(s1, s2, s3)] = s1 == s3 if not s2 else s2 == s3
            return self.res[(s1, s2, s3)]
        if s1[0] == s3[0] and s2[0] == s3[0]:
            self.res[(s1, s2, s3)] = self.reInterleave(s1[1:], s2, s3[1:]) or self.reInterleave(s1, s2[1:], s3[1:])
        elif s1[0] == s3[0]:
            self.res[(s1, s2, s3)] = self.reInterleave(s1[1:], s2, s3[1:])
        elif s2[0] == s3[0]:
            self.res[(s1, s2, s3)] = self.reInterleave(s1, s2[1:], s3[1:])
        else:
            self.res[(s1, s2, s3)] = False
        return self.res[(s1, s2, s3)]


if __name__ == '__main__':
    s = Solution()
    s1 = "aacaac"
    s2 = "aacaaeaac"
    s3 = "aacaacaaeaacaac"
    print(s.isInterleave(s1, s2, s3))
