#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 8:53
# @Author  : qkwu
# @File    : leetcode45JumpGameII.py

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        curRea = 0
        curMax = 0
        res = 0
        for i in range(length):
            if i > curRea:
                res += 1
                curRea = curMax
            curMax = max(curMax, nums[i]+i)
        return res



nums = [2,3,1,1,4]
sl = Solution()
print(sl.jump(nums))