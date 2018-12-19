#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:44
# @Author  : qkwu
# @File    : leetcode50PowXN.py

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            return 1.0 / self.myPow(x, -n)
        else:
            half = self.myPow(x, n//2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x