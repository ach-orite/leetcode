#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:42
# @Author  : qkwu
# @File    : leetcode35SearchInsertPostion.py

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0]>target:
            return 0
        if nums[-1]<target:
            return len(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            elif nums[i]>target and i!=0:
                return i