# -*- coding: utf-8 -*-
# @File  : 72_EditDistance.py
# @Author: ZRN
# @Date  : 2019/5/13
"""
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))
        m = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for i in range(len(m[0])):
            m[0][i] = i
        for i in range(len(m)):
            m[i][0] = i
        for i in range(1, len(m)):
            for j in range(1, len(m[0])):
                if word1[j - 1] == word2[i - 1]:
                    m[i][j] = m[i - 1][j - 1]
                else:
                    m[i][j] = min(m[i - 1][j], m[i][j - 1], m[i - 1][j - 1]) + 1
        return m[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance('horse', 'ros'))
