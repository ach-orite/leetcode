#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:36
# @Author  : qkwu
# @File    : leetcode15ThreeSum.py

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                j, k = i+1, len(nums)-1
                while j < k:
                    while j < k and nums[j] + nums[k] + nums[i] < 0 :
                        j += 1
                    while j < k and nums[j] + nums[k] + nums[i] > 0:
                        k -= 1
                    if j == k :
                        break
                    if nums[j] + nums[k] + nums[i] == 0 :
                        res.append([nums[i], nums[j], nums[k]])

                        while j < k and nums[j] == nums[j+1]:
                            j += 1
                        while j < k and nums[k] == nums[k-1]:
                            k -= 1
                        j += 1
                        k -= 1

        return res
