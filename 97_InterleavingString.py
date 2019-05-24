# -*- coding: utf-8 -*-
# @File  : 97_InterleavingString.py
# @Author: ZRN
# @Date  : 2019/5/24
"""
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return True if s2 == s3 else False
        if not s2:
            return True if s1 == s3 else False
        return self.reInterleave(s1, s2, s3)

    def reInterleave(self, s1: str, s2: str, s3: str) -> bool:
        print(s3)
        if not s1:
            return True if s2 == s3 else False
        if not s2:
            return True if s1 == s3 else False
        if s1[0] == s3[0] and s2[0] == s3[0]:
            return self.reInterleave(s1[1:], s2, s3[1:]) or self.reInterleave(s1, s2[1:], s3[1:])
        elif s1[0] == s3[0]:
            return self.reInterleave(s1[1:], s2, s3[1:])
        elif s2[0] == s3[0]:
            return self.reInterleave(s1, s2[1:], s3[1:])
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    print(s.reInterleave(s1, s2, s3))
