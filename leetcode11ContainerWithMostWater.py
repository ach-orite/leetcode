#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:36
# @Author  : qkwu
# @File    : leetcode11ContainerWithMostWater.py

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        length = len(height)
        i, j = 0, length - 1
        while i < j:
            h = min(height[i], height[j])
            res = max(res, h * (j - i))
            if h == height[j]:
                while i < j and height[j] <= h:
                    j -= 1
            elif h == height[i]:
                while i < j and height[i] <= h:
                    i += 1
        return res
