# -*- coding: utf-8 -*-
# @File  : solveNQueens.py
# @Author: ZRN
# @Date  : 2018/10/30
"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
"""
import copy


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n <= 0:
            return []
        if n == 1:
            return [['Q']]
        board = [['#'] * n for _ in range(n)]
        res = self.solveNQueens_it(board, n, n ** 2)
        res_str = []
        for re in res:
            res_str.append([''.join(row) for row in re])
        return res_str

    def solveNQueens_it(self, board, n, m):
        if n == 0:
            return [board]
        if n > m and '#' not in board[len(board) - n]:
            return []

        row = len(board) - n
        res = []
        for i in range(len(board)):
            if board[row][i] == '#':
                new_board = copy.deepcopy(board)
                m_copy = m
                new_board[row][i] = 'Q'
                m_copy -= 1
                for j in range(len(board)):
                    if new_board[row][j] == '#':
                        m_copy -= 1
                        new_board[row][j] = '.'

                for j in range(row + 1, len(board)):
                    if new_board[j][i] == '#':
                        m_copy -= 1
                        new_board[j][i] = '.'

                r = row + 1
                cl = i - 1
                cr = i + 1
                while r < len(board):
                    if cl >= 0 and new_board[r][cl] == '#':
                        m_copy -= 1
                        new_board[r][cl] = '.'
                    if cr < len(board) and new_board[r][cr] == '#':
                        m_copy -= 1
                        new_board[r][cr] = '.'

                    cr += 1
                    cl -= 1
                    r += 1
                res += self.solveNQueens_it(new_board, n - 1, m_copy)
        return res


if __name__ == '__main__':
    s = Solution()
    for b in s.solveNQueens(5):
        for row in b:
            print(row)
        print()

