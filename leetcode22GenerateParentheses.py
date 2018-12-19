#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:39
# @Author  : qkwu
# @File    : leetcode22GenerateParentheses.py

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(left, right ,str):
            if left < right:
                return
            elif left == right and right == n:
                res.append(str)
                return
            elif left > n:
                return
            dfs(left + 1, right, str+'(')
            dfs(left, right + 1, str+')')
        dfs(0, 0, '')
        return res