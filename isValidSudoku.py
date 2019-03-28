# -*- coding: utf-8 -*-
# @File  : isValidSudoku.py
# @Author: ZRN
# @Date  : 2018/10/8
"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

1. 数字 1-9 在每一行只能出现一次。
2. 数字 1-9 在每一列只能出现一次。
3. 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
"""


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_sets = [''] * 9
        column_sets = [''] * 9
        area_sets = [[''] * 3 for _ in range(3)]
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char != '.':
                    if char not in row_sets[i]:
                        row_sets[i] += char
                    else:
                        return False
                    if char not in column_sets[j]:
                        column_sets[j] += char
                    else:
                        return False
                    if char not in area_sets[i // 3][j // 3]:
                        area_sets[i // 3][j // 3] += char
                    else:
                        return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                           [".", "9", "8", ".", ".", ".", ".", "6", "."],
                           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                           [".", "6", ".", ".", ".", ".", "2", "8", "."],
                           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
