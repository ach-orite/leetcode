#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 15:56
# @Author  : qkwu
# @File    : leetcode56LengthofThelastWord.py

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        data = s.strip().split(' ')
        if not data:
            return 0
        else:
            return len(data[-1])
str = 'a '
sl = Solution()
print(sl.lengthOfLastWord(str))