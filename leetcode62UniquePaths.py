#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 9:35
# @Author  : qkwu
# @File    : leetcode62UniquePaths.py

# dfs方法 超时
# class Solution:
#     def uniquePaths(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         self.res = 0
#         self.dfs(m, n, 1, 1)
#         return self.res
#
#     def dfs(self, m, n, r, c):
#         if r == m and c == n:
#             self.res += 1
#             return
#         elif r > m or c > n:
#             return
#         else:
#             self.dfs(m, n, r + 1, c)
#             self.dfs(m, n, r, c + 1)


#dp方法 p(m,n) = p(m-1,n)+p(m,n-1)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1

        dp = [[int(1) for i in range(m)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]



#Output: 28

sl = Solution()
print(sl.uniquePaths(7, 3))