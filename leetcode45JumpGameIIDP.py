#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 9:33
# @Author  : qkwu
# @File    : leetcode45JumpGameIIDP.py
import sys

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [sys.maxsize] * length
        dp[0] = 0
        for i in range(1, length):
            for j in range(0, i):
                if i - j <= nums[j]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]





nums = [2,3,1,1,4]
sl = Solution()
print(sl.jump(nums))