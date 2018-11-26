#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 9:36
# @Author  : qkwu
# @File    : leetcode63UniquePathsII.py

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1: continue
                if i == 0 and j == 0: dp[i][j] = 1
                elif i == 0: dp[i][j] = dp[i][j-1]
                elif j == 0: dp[i][j] = dp[i-1][j]
                else: dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
#Output: 2

sl = Solution()
print(sl.uniquePathsWithObstacles(obstacleGrid))
