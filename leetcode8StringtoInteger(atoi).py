#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:35
# @Author  : qkwu
# @File    : leetcode8StringtoInteger(atoi).py

import re

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        pattern = r'[\s]*[+-]?[\d]+'
        match = re.match(pattern, str)
        if match:
            res = int(match.group(0))
        else:
            res = 0
        return max(-2 ** 31, min(res, 2 ** 31 - 1))