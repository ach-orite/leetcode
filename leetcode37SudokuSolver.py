#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:43
# @Author  : qkwu
# @File    : leetcode37SudokuSolver.py

class Solution:
    def isValidSudoku(self, board, row, col, k):
        for i in range(9):
            if board[row][i] != '.' and board[row][i] == k:
                return False
        for j in range(9):
            if board[j][col] != '.' and board[j][col] == k:
                return False
        r1 = (row // 3) * 3
        c1 = (col // 3) * 3
        for i in range(r1, r1+3):
            for j in range(c1, c1+3):
                if board[i][j] != '.' and board[i][j] == k:
                    return False
        return True

    def solveSudoku(self, board):
        self.board = board
        self.solve(board)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(1,10):
                        if self.isValidSudoku(board, i, j, str(k)):
                            board[i][j] = str(k)
                            if self.solve(board):
                                return True
                        board[i][j] = '.'
                    return False
        return True