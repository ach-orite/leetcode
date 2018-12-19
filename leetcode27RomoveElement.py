#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:40
# @Author  : qkwu
# @File    : leetcode27RomoveElement.py

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        removed = 0
        for i in range(0, len(nums)):
            if nums[i] == val:
                removed += 1
            else:
                nums[i - removed] = nums[i]

        return len(nums) - removed