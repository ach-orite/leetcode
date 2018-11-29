#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 15:46
# @Author  : qkwu
# @File    : leetcode90SubSetII.py

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = set()
        self.dfs(nums, res, [])
        realres = []
        for tup in res:
            realres.append(list(tup))
        return realres

    def dfs(self, nums, res, temp):
        if not nums:
            res.add(tuple(temp))
        else:
            self.dfs(nums[1:], res, temp[:])
            temp.append(nums[0])
            self.dfs(nums[1:], res, temp[:])


nums = [1,2,2]
Output = [
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

sl = Solution()
print(sl.subsetsWithDup(nums))