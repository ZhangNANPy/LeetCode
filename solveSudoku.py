# -*- coding: utf-8 -*-
# @File  : solveSudoku.py
# @Author: ZRN
# @Date  : 2018/10/8
"""
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

1. 数字 1-9 在每一行只能出现一次。
2. 数字 1-9 在每一列只能出现一次。
3. 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
"""

import copy


class Solution:
    def __init__(self):
        self.all_nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        res = self.solve_sudoku_it(board)
        for i in range(9):
            for j in range(9):
                board[i][j] = res[i][j]

    def solve_sudoku_it(self, board):
        """
        :type board: List[List[str]]
        :rtype: mix: False or List[List[str]]
        """
        if self.simple_solve_sudoku(board):
            return board

        row_sets = [set() for _ in range(9)]
        column_sets = [set() for _ in range(9)]
        area_sets = [[set() for _ in range(3)] for _ in range(3)]
        first_point = None
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char != '.':
                    row_sets[i].add(char)
                    column_sets[j].add(char)
                    area_sets[i // 3][j // 3].add(char)
                elif not first_point:
                    first_point = (i, j)

        nums = self.all_nums - row_sets[first_point[0]] - column_sets[first_point[1]] \
               - area_sets[first_point[0] // 3][first_point[1] // 3]
        for num in nums:
            copy_board = copy.deepcopy(board)
            copy_board[first_point[0]][first_point[1]] = num
            re_board = self.solve_sudoku_it(copy_board)
            if re_board:
                return re_board
        return False

    def simple_solve_sudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_sets = [set() for _ in range(9)]
        column_sets = [set() for _ in range(9)]
        area_sets = [[set() for _ in range(3)] for _ in range(3)]
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char != '.':
                    row_sets[i].add(char)
                    column_sets[j].add(char)
                    area_sets[i // 3][j // 3].add(char)

        flag = True
        while flag:
            flag = False
            for i, row in enumerate(board):
                for j, char in enumerate(row):
                    if char == '.':
                        num_set = self.all_nums - row_sets[i] - column_sets[j] - area_sets[i // 3][j // 3]
                        if len(num_set) == 1:
                            flag = True
                            num = num_set.pop()
                            row_sets[i].add(num)
                            column_sets[j].add(num)
                            area_sets[i // 3][j // 3].add(num)
                            board[i][j] = num

        for row in board:
            if '.' in row:
                return False
        return True

    @staticmethod
    def print_matrix(matrix):
        for row in matrix:
            print(row)
        return


if __name__ == '__main__':
    s = Solution()
    m = [[".", ".", "5", "3", ".", ".", ".", ".", "."],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", "7", ".", ".", "1", ".", "5", ".", "."],
         ["4", ".", ".", ".", ".", "5", "3", ".", "."],
         [".", "1", ".", ".", "7", ".", ".", ".", "6"],
         [".", ".", "3", "2", ".", ".", ".", "8", "."],
         [".", "6", ".", "5", ".", ".", ".", ".", "9"],
         [".", ".", "4", ".", ".", ".", ".", "3", "."],
         [".", ".", ".", ".", ".", "9", "7", ".", "."]]

    import time

    start = time.clock()
    s.solveSudoku(m)
    finish = time.clock()
    print((finish - start) / 1000000)
    s.print_matrix(m)
