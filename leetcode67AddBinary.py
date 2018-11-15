#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 10:54
# @Author  : qkwu
# @File    : leetcode67AddBinary.py

# use python built_in
# class Solution:
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         return bin(eval('0b'+a)+eval('0b'+b))[2:]

class Solution:
    def addBinary(self, a, b):
        i, j, c = len(a) - 1, len(b) - 1, 0
        # c表示是否进位
        ans = ""
        while i >= 0 or j >= 0 or c:
            c += ord(a[i]) - ord("0") if i >= 0 else 0
            c += ord(b[j]) - ord("0") if j >= 0 else 0
            ans = chr((c & 1) + ord("0")) + ans
            i -= 1
            j -= 1
            c >>= 1    #将c右移，进位的成功移到下一位
        return ans

a = "1010"
b = "1011"
sl = Solution()
print(sl.addBinary(a, b))