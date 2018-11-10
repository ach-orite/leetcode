#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 11:21
# @Author  : qkwu
# @File    : leetcode55JumpGame.py
import math
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for i in range(len(nums)-1):
            if i <= reach:
                reach = max(reach, i+nums[i])
        return reach >= len(nums)-1


nums = [2,3,1,1,4]
sl = Solution()
print(sl.canJump(nums))