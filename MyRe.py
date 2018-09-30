# -*- coding: utf-8 -*-
"""
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == '' and p == '':
            return True
        if s != '' and p == '':
            return False
        if s == '' and p != '':
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:])
            else:
                return False
        if len(p) > 1 and p[1] == '*':
            if p[0] == '.'or p[0] == s[0]:
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                return self.isMatch(s, p[2:])
        else:
            if s[0] == p[0] or p[0] == '.':
                return self.isMatch(s[1:], p[1:])
            else:
                return False


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch('mississippi', 'mis*is*p*.'))

