# -*- coding: utf-8 -*-
# @File  : 93_RestoreIPAddresses.py
# @Author: ZRN
# @Date  : 2019/5/23
"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
"""


class Solution:
    def restoreIpAddresses(self, s: str):
        self.ress = []
        self.IPpart([], s, 4)
        return self.ress

    def IPpart(self, res, s, n):
        if not n and not s and len(res) == 4:
            self.ress.append('.'.join(res))
            return
        if n <= 0:
            return
        if len(s) / n > 3 or len(s) / n < 1:
            return
        t = res[:]
        t.append(s[:1])
        self.IPpart(t, s[1:], n - 1)
        if len(s) >= 2 and s[0] != '0':
            t = res[:]
            t.append(s[:2])
            self.IPpart(t, s[2:], n - 1)
        if len(s) >= 3 and int(s[:3]) < 256 and s[0] != '0':
            t = res[:]
            t.append(s[:3])
            self.IPpart(t, s[3:], n - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses('0000'))
