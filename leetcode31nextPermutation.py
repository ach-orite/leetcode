#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 11:41
# @Author  : qkwu
# @File    : leetcode31nextPermutation.py

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for k in range(length - 1, -1, -1):
                    if nums[k] > nums[i]:
                        nums[i], nums[k] = nums[k], nums[i]
                        nums[i+1:] = sorted(nums[i+1:])
                        return nums
        return nums


nums = [3,4,2,1]
sl = Solution()
print(sl.nextPermutation(nums))
