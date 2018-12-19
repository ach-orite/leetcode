#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:44
# @Author  : qkwu
# @File    : leetcode48RotateImage.py

class Solution:
    def rotate(self, matrix):
        m = matrix
        n = len(matrix)
        l = n-1
        for i in range(n//2):
            for j in range(i, l-i):
                m[j][l-i], m[l-i][l-j], m[l-j][i], m[i][j] = m[i][j], m[j][l-i], m[l-i][l-j], m[l-j][i]