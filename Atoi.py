# -*- coding: utf-8 -*-
"""
在找到第一个非空字符之前，需要移除掉字符串中的空格字符。如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。

当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。

若函数不能执行有效的转换，返回 0。
"""


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        nsstr = str.split()
        if not nsstr:
            return 0
        nsstr = nsstr[0]
        flag = 1
        if nsstr[0] == '-' or nsstr[0] == '+':
            flag = nsstr[0]
            nsstr = nsstr[1:]
            if flag == '-':
                flag = -1
            else:
                flag = 1
        if not nsstr:
            return 0
        i = 0
        while i < len(nsstr) and nsstr[i].isdigit():
                i += 1
        nsstr = nsstr[:i]
        if nsstr:
            num = flag * int(nsstr)
            if -1 * 2 ** 31 <= num <= 2 ** 31 -1:
                return num
            elif num < -1 * 2 ** 31:
                return -1 * 2 ** 31
            else:
                return 2 ** 31 -1
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi(''))
