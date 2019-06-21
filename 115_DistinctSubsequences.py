# -*- coding: utf-8 -*-
# @File  : 115_DistinctSubsequences.py
# @Author: ZRN
# @Date  : 2019/6/21
"""
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        if s == t:
            return 1
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        dp[0] = [1] * (len(s) + 1)
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if t[i] == s[j]:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]
