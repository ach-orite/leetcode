#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:43
# @Author  : qkwu
# @File    : leetcode38CountAndSay.py

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = '1'
        if n == 1:
            return seq
        else:
            for _ in range(1, n):
                i, j = 0, 0
                count = 1
                newseq = ''
                while j < len(seq)-1:
                    j = j + 1
                    if seq[i] == seq[j]:
                        count += 1
                    elif seq[i] != seq[j]:
                        newseq += str(count)
                        newseq += seq[i]
                        count = 1
                        i = j
                newseq += str(count)
                newseq += seq[i]
                seq = newseq
            return seq
