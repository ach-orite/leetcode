
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 16:03
# @Author  : qkwu
# @File    : leetcode70ClimbingStairs.py

class Solution:
    def climbStairs(self, n):
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a
n = 35
Sl = Solution()
print(Sl.climbStairs(n))