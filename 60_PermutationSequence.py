# -*- coding: utf-8 -*-
# @File  : 60_PermutationSequence.py
# @Author: ZRN
# @Date  : 2019/4/29
"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

1"123"
2"132"
3"213"
4"231"
5"312"
6"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 0 and k == 1:
            return '1'
        nums = [i + 1 for i in range(n)]
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[i - 1] * i)
        if k > factorial[-1] * n:
            return ''
        res = ''
        for i in range(n):
            cur_num = (k - 1) // factorial[-1]
            k = k % factorial[-1]
            del factorial[-1]
            res += str(nums[cur_num])
            del nums[cur_num]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(4, 9))
