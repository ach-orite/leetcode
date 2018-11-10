#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 11:21
# @Author  : qkwu
# @File    : leetcode55JumpGame.py

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i_left = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):  # go backward
            if i + nums[i] >= i_left:  # if maximum jump is far enough
                i_left = i
        return i_left == 0


nums = [2,3,1,1,4]
sl = Solution()
print(sl.canJump(nums))