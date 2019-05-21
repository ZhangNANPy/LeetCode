# -*- coding: utf-8 -*-
# @File  : 76_MinimumWindowSubstring.py
# @Author: ZRN
# @Date  : 2019/5/14
"""
给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        letter_count = {}
        cur_letter = {}
        for c in t:
            cur_letter[c] = 0
            if c in letter_count:
                letter_count[c] += 1
            else:
                letter_count[c] = 1
        letter_list = []
        index_list = []
        min_sub = [0, len(s) * 2]
        all_letter = False
        for i, c in enumerate(s):
            if c in letter_count:
                letter_list.append(c)
                index_list.append(i)
                cur_letter[c] += 1
                while cur_letter[letter_list[0]] > letter_count[letter_list[0]]:
                    cur_letter[letter_list[0]] -= 1
                    del letter_list[0]
                    del index_list[0]
                if all_letter:
                    if (min_sub[1] - min_sub[0]) > (index_list[-1] - index_list[0]):
                        min_sub[0] = index_list[0]
                        min_sub[1] = index_list[-1]
                else:
                    for j in letter_count:
                        if letter_count[j] > cur_letter[j]:
                            break
                    else:
                        all_letter = True
                        min_sub[0] = index_list[0]
                        min_sub[1] = index_list[-1]
        if min_sub[1] - min_sub[0] + 1 <= len(s):
            return s[min_sub[0]: min_sub[1] + 1]
        return ''

    def minWindow2(self, s, t):
        from collections import defaultdict
        i = j = 0
        count = len(t)
        step = float("inf")
        res = ""
        dic = defaultdict(int)
        for e in t:
            dic[e] += 1
        while j < len(s):
            if dic[s[j]] > 0:
                count -= 1
            dic[s[j]] -= 1  # t之外的字符数据为负，s中所有出现的字母都记录
            j += 1
            while count == 0:
                if step > j - i:
                    step = j - i
                    res = s[i:j]
                if dic[s[i]] == 0:  # t中的字母才为0
                    count += 1
                dic[s[i]] += 1
                i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow2("acadb", "ab"))
