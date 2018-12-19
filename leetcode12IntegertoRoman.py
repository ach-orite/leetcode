#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:36
# @Author  : qkwu
# @File    : leetcode12IntegertoRoman.py

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        base = 1000
        trans = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        while num > 0:
            val, num = divmod(num, base)
            if val <= 3:
                res += trans[base] * val
            elif val == 4:
                res += trans[base]
                res += trans[base*5]
            elif val == 9:
                res += trans[base]
                res += trans[base*10]
            else:
                res += trans[base*5]
                res += trans[base]*(val-5)

            base //= 10
        return res