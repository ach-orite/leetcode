#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 9:54
# @Author  : qkwu
# @File    : leetcode43MultiplyStrings.py

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = 0
        for i in range(len(num1)):
            for j in range(len(num2)):
                ans += ((ord(num1[-i - 1]) - ord('0')) * 10 ** i) * ((ord(num2[-j - 1]) - ord('0')) * 10 ** j)
        return str(ans) 

num1 = "123"
num2 = "456"
#Output: "56088"
sl = Solution()
print(sl.multiply(num1, num2))