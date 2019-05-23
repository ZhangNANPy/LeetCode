# -*- coding: utf-8 -*-
# @File  : 91_DecodeWays.py
# @Author: ZRN
# @Date  : 2019/5/23
"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。
"""


class Solution:
    def __init__(self):
        self.res = {}
        for i in range(10):
            self.res[str(i)] = 1
        self.res['0'] = 0
        self.res[''] = 1

    def numDecodings(self, s: str) -> int:
        print(s)
        if s and s[0] == '0':
            return 0
        if not s:
            return 1
        if s in self.res:
            return self.res[s]
        if int(s[:2]) <= 26:
            self.res[s] = (self.res[s[1:]] if s[1:] in self.res else self.numDecodings(s[1:])) + \
                          (self.res[s[2:]] if s[2:] in self.res else self.numDecodings(s[2:]))
        else:
            self.res[s] = self.res[s[1:]] if s[1:] in self.res else self.numDecodings(s[1:])
        return self.res[s]


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("12"))
