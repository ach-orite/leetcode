#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:40
# @Author  : qkwu
# @File    : leetcode28ImplementstrStr().py

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)