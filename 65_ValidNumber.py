# -*- coding: utf-8 -*-
# @File  : 65_ValidNumber.py
# @Author: ZRN
# @Date  : 2019/4/30
"""
验证给定的字符串是否可以解释为十进制数字。
"""


class Solution:
    # re: r'^\s*[\-\+]?((\.[0-9]+)|([0-9]+(\.[0-9]*)?))([eE][\-\+]?[0-9]+)?\s*$'
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        nums = s.split('e')
        if len(nums) > 2:
            return False
        if len(nums) == 2:
            return self.isDigit(nums[0]) and self.isInteger(nums[1])
        else:
            return self.isDigit(nums[0])

    def isDigit(self, s):
        if not s:
            return False
        nums = s.split('.')
        if len(nums) > 2:
            return False

        i = self.isInteger(nums[0])
        ie = self.isEmptyInt(nums[0])
        if len(nums) == 2:
            d = nums[1].isdigit()
            de = nums[1] == ''
            return (i and d) or (ie and d) or (i and de)
        return i

    def isInteger(self, s):
        if not s:
            return False

        if s[0] == '+' or s[0] == '-':
            s = s[1:]

        if not s.isdigit():
            return False

        if s[0] == '0' and len(s[0]) > 1:
            return False
        return True

    def isEmptyInt(self, s):
        if not s or (len(s) == 1 and (s == '+' or s == '-')):
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isNumber("+.3"))
