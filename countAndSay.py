# -*- coding: utf-8 -*-
# @File  : countAndSay.py
# @Author: ZRN
# @Date  : 2018/10/9
"""
报数序列是指一个整照其中的整数的顺序进数序列，按行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        last = '1'
        cur = '1'
        for _ in range(n - 1):
            cur = ''
            count = 1
            last_num = last[0]
            for i in range(1, len(last)):
                if last[i] == last_num:
                    count += 1
                else:
                    cur += str(count) + last_num
                    count = 1
                    last_num = last[i]
            cur += str(count) + last_num
            last = cur
        return cur


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(5))
