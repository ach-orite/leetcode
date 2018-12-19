#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:41
# @Author  : qkwu
# @File    : leetcode33SearchinRotatedSortedArray.py

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]:
                if nums[left]<=target and target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            if nums[mid]<=nums[right]:
                if nums[mid]<target and target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1