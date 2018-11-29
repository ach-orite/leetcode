#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 15:48
# @Author  : qkwu
# @File    : leetcode75SortColors.py

# 三指针法， 记录最后一个
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        i, j, k = -1, -1, -1
        for num in nums:
            if num == 0:
                k += 1
                nums[k] = 2
                j += 1
                nums[j] = 1
                i += 1
                nums[i] = 0
            elif num == 1:
                k += 1
                nums[k] = 2
                j += 1
                nums[j] = 1
            else:
                k += 1
                nums[k] = 2
        return

nums = [2, 0, 2, 1, 1, 0]
# Output: [0,0,1,1,2,2]

sl = Solution()
sl.sortColors(nums)
print(nums)