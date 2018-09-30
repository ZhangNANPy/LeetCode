# -*- coding: utf-8 -*-
"""
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，
所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

* I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
* X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
* C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
"""


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = {0: '', 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        res = ''
        magnitude = 1
        while num > 0:
            temp = ''
            for ros in self.getRomanStructure(num % 10):
                temp += roman[ros[0] * magnitude] * ros[1]
            res = temp + res
            num //= 10
            magnitude *= 10
        return res

    def getRomanStructure(self, num):
        ros = {0: [], 1: [[1, 1]], 2: [[1, 2]], 3: [[1, 3]], 4: [[1, 1], [5, 1]], 5: [[5, 1]], 6: [[5, 1], [1, 1]],
               7: [[5, 1], [1, 2]], 8: [[5, 1], [1, 3]], 9: [[1, 1], [10, 1]], 10: [[10, 1]]}
        return ros[num]
