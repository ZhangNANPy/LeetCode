# -*- coding: utf-8 -*-
"""
给定一个字符串，找出不含有重复字符的最长子串的长度。
注意子序列和子串的区别
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        sub_str = {}
        sub_str_begin = 0
        for i in range(len(s)):
            try:
                if sub_str[s[i]] >= sub_str_begin:
                    sub_str_begin = sub_str[s[i]] + 1
            except KeyError:
                pass
            max_len = max(i - sub_str_begin + 1, max_len)
            sub_str[s[i]] = i
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcbb'))