#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:42
# @Author  : qkwu
# @File    : leetcode34FindFirstAndLastPositionofElementinSortedArray.py

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first, last = -1, -1
        left, right = 0, len(nums)-1
        Found = False
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first = last = mid
                Found = True
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if not Found:
            return [-1, -1]
        else:
            ln, rn = 0, len(nums)-1
            while ln <= mid:
                lmid = (mid - ln) // 2 + ln
                if target == nums[lmid]:
                    first = lmid
                    mid = lmid - 1
                else:
                    ln = lmid + 1
            while mid <= rn:
                rmid = (rn - mid) // 2 + mid
                if target == nums[rmid]:
                    last = rmid
                    mid = rmid + 1
                else:
                    rn = rmid - 1
            res = [first] + [last]
            return res