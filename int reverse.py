# -*- coding: utf-8 -*-
"""
给定一个 32 位有符号整数，将整数中的数字进行反转。
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            flag = -1
            x = int(str(x)[:0:-1])
            # a[x:y:-1]是先反转再截断的，但是截断时用的还是之前序列的索引。
            # 故x>y,且y>=0,序列中不包含y。要获取完整的序列末尾，只能省略y。
        else:
            x = int(str(x)[::-1])
            flag = 1
        if -1 * 2 ** 31 <= x <= 2 ** 31 - 1:
            return x * flag
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-123))
