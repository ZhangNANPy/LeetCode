# -*- coding: utf-8 -*-
# @File  : totalNQueens.py
# @Author: ZRN
# @Date  : 2018/10/31
"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回 n 皇后不同的解决方案的数量。
"""


class Solution:
    """
     把棋盘存储为一个N维数组a[N]，数组中第i个元素的值代表第i行的皇后位置，这样便可以把问题的空间规模压缩为一维O(N).
     在判断是否冲突时也很简单，首先每行只有一个皇后，且在数组中只占据一个元素的位置，行冲突就不存在了;
     列冲突，判断一下是否有a[i]与当前要放置皇后的列j相等即可;
     斜线冲突，所有在斜线上冲突的皇后的位置都有规律即它们所在的行列互减的绝对值相等，即| row – i | = | col – a[i] | .
     这样某个位置是否可以放置皇后的问题已经解决。
    """
    def __init__(self):
        self.counter = 0

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        board = [-1] * n
        self.totalNQueens_it(board, 0)
        return self.counter

    def totalNQueens_it(self, board, row):
        if row == len(board):
            self.counter += 1
            return
        for i in range(len(board)):
            if self.check_place(board, row, i):
                board[row] = i
                self.totalNQueens_it(board, row + 1)

    def check_place(self, board, row, col):
        for i in range(row):
            if board[i] == col or row - i == abs(board[i] - col):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.totalNQueens(5))
