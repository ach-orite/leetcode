#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 16:39
# @Author  : qkwu
# @File    : leetcode78Subsets.py

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, res, [])
        return res

    def dfs(self, nums, res, temp):
        if not nums:
            res.append(temp)
        else:
            reslist = temp[:]
            self.dfs(nums[1:], res, reslist)
            temp.append(nums[0])
            reslist = temp[:]
            self.dfs(nums[1:], res, reslist)




nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

sl = Solution()
print(sl.subsets(nums))