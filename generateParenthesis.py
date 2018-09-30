# -*- coding: utf-8 -*-
# @File  : generateParenthesis.py
# @Author: ZRN
# @Date  : 2018/9/27
"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n):
        self.cache = {}
        return list(self.generateParenthesis2(n))

    def generateParenthesisIt(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        if n == 1:
            return ['()']
        if n in self.cache.keys():
            return self.cache[n]
        res = set()
        for i in range(1, n // 2 + 1):
            pl1 = self.generateParenthesisIt(i)
            pl2 = self.generateParenthesisIt(n - i)
            for p1 in pl1:
                res |= {'(' * (n - i) + p1 + ')' * (n - i)}
                for p2 in pl2:
                    res |= {p1 + p2, p2 + p1}
        for i in range(n // 2 + 1, n):
            pl1 = self.generateParenthesisIt(i)
            for p1 in pl1:
                res |= {'(' * (n - i) + p1 + ')' * (n - i)}
        self.cache[n] = res
        return res

    def generateParenthesis2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n in self.cache.keys():
            return self.cache[n]
        if n == 0:
            self.cache[n] = ['']
        else:
            answer = []
            for i in range(n):
                answer = answer + ['(' + e1 + ')' + e2
                                   for e1 in self.generateParenthesis(i)
                                   for e2 in self.generateParenthesis(n - 1 - i)]
            self.cache[n] = answer
        return self.cache[n]


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(4))
