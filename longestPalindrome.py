# -*- coding: utf-8 -*-
"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        sub_str = [0, 1]
        palindromes = []
        len_sub_str = 1
        for i in range(2, len(s)):
            j = 0
            while j < len(palindromes):
                if palindromes[j] - 1 >= 0 and s[palindromes[j] - 1] == s[i]:
                    palindromes[j] = palindromes[j] - 1
                    j = j + 1
                else:
                    if i - palindromes[j] > len_sub_str:
                        len_sub_str = i - palindromes[j]
                        sub_str = [palindromes[j], i]
                    del palindromes[j]
            if s[i] == s[i-1]:
                palindromes.append(i - 1)
            if s[i] == s[i - 2]:
                palindromes.append(i - 2)
        for i in palindromes:
            if len(s) - i > len_sub_str:
                sub_str = [i, len(s)]
                len_sub_str = len(s) - 1
        if s[0] == s[1] and len_sub_str < 2:
            return s[0: 2]
        return s[sub_str[0]: sub_str[1]]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('ccc'))
