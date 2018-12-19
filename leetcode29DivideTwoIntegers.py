#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:40
# @Author  : qkwu
# @File    : leetcode29DivideTwoIntegers.py

class Solution:
    def divide(self, dividend, divisor):

        # this is necessary; otherwise phase 1 never terminates
        if dividend == 0: return 0

        # initialize
        i, result, p, q = map(abs, (0, 0, dividend, divisor))

        # phase 1
        while q << i <= p: i += 1

        # phase 2
        for j in reversed(range(i)):
            if q << j <= p: p, result = p - (q << j), result + (1 << j)

        # stupid leetcode restrictions
        if (dividend > 0) != (divisor > 0) or result < -1 << 31:
            result = -result
        return min(result, (1 << 31) - 1)