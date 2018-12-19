#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 15:10
# @Author  : qkwu
# @File    : leetcode89GrayCode.py

"""
这种方法基于格雷码是反射码的事实，利用递归的如下规则来构造：

1位格雷码有两个码字
(n+1)位格雷码中的前2n个码字等于n位格雷码的码字，按顺序书写，加前缀0
(n+1)位格雷码中的后2n个码字等于n位格雷码的码字，按逆序书写，加前缀1
n+1位格雷码的集合 = n位格雷码集合(顺序)加前缀0 + n位格雷码集合(逆序)加前缀1
"""

#GrayCode  Definition
class Solution(object):
    def grayCode(self, n):
        return [(num ^ (num >> 1)) for num in range(2 ** n)]
