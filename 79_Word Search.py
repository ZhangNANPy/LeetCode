# -*- coding: utf-8 -*-
# @File  : 79_Word Search.py
# @Author: ZRN
# @Date  : 2019/5/15
"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。
"""


class Solution:
    def exist(self, board, word: str) -> bool:
        if not word:
            return False
        self.flag_board = [[True] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    curi = i
                    curj = j
                    stack = []
                    while len(stack) < len(word):  # 针对当前节点的写法比较简单
                        if self.is_right(curi, curj) and word[len(stack)] == board[curi][curj]:
                            stack.append([curi, curj, 0])
                            self.flag_board[curi][curj] = False
                            curi, curj = self.get_next(curi, curj, 0)
                        else:
                            while stack:
                                if stack[-1][-1] < 3:
                                    curi, curj = self.get_next(stack[-1][0], stack[-1][1], stack[-1][-1] + 1)
                                    stack[-1][-1] += 1
                                    break
                                else:
                                    curi, curj, dir = stack.pop()
                                    self.flag_board[curi][curj] = True
                            else:
                                break
                    else:
                        return True
        return False

    def get_next(self, i, j, dir):
        if dir == 0:  # right
            return i, j + 1
        if dir == 1:  # down
            return i + 1, j
        if dir == 2:  # left
            return i, j - 1
        if dir == 3:  # up
            return i - 1, j
        return -1, -1

    def is_right(self, i, j):
        if 0 <= i < len(self.flag_board) and 0 <= j < len(self.flag_board[i]) and self.flag_board[i][j]:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    m = [['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']]
    print(s.exist(m, "ABCCED"))
