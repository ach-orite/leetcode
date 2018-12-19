#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:42
# @Author  : qkwu
# @File    : leetcode36ValidSudoku.py

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        sudoku = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    cur = board[i][j]
                    if (i, cur) in sudoku or (cur, j) in sudoku or (i // 3, j // 3, cur) in sudoku:
                        return False
                    sudoku.add((i, cur))
                    sudoku.add((cur, j))
                    sudoku.add((i // 3, j // 3, cur))
        return True
