#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 14:37
# @Author  : qkwu
# @File    : leetcode64MinumumPathSum.py

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        #print(dp)
        dp[0][0] = grid[0][0]
        for i in range(1, cols):
            dp[0][i] = dp[0][i-1]+grid[0][i]
        for j in range(1, rows):
            dp[j][0] = dp[j-1][0] + grid[j][0]

        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min((dp[i][j-1]+grid[i][j]), (dp[i-1][j] + grid[i][j]))
        return dp[rows-1][cols-1]

Input = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

sl = Solution()
print(sl.minPathSum(Input))