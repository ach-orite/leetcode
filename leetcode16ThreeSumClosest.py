#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:37
# @Author  : qkwu
# @File    : leetcode16ThreeSumClosest.py

import sys
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = sys.maxsize
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k :
                if abs(nums[i] + nums[j] + nums[k] - target) < abs(res - target):
                    res = nums[i] + nums[j] + nums[k]
                if nums[i] + nums[j] + nums[k] == target:
                    res = nums[i] + nums[j] + nums[k]
                    break
                if nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                    continue
                if nums[i] + nums[j] + nums[k] < target:
                    j += 1
                    continue

        return res

