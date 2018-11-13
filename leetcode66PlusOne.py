#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 16:30
# @Author  : qkwu
# @File    : leetcode66PlusOne.py

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = 0
        for i in range(len(digits)):
            res *= 10
            res += digits[i]
        res += 1
        li = list(str(res))
        for _ in range(len(li)):
            li[_] = int(li[_])
        return li
nums = [1,2,3]
sl = Solution()
print(sl.plusOne(nums))