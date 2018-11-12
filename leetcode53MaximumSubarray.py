#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 15:32
# @Author  : qkwu
# @File    : leetcode53MaximumSubarray.py
import sys
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            sum, res = 0, -sys.maxsize-1
            for i in range(len(nums)):
                sum += nums[i]
                res = max(res, sum)
                if sum < 0:
                    sum = 0
            return res


nums = [-2,1,-3,4,-1,2,1,-5,4]
sl = Solution()
print(sl.maxSubArray(nums))