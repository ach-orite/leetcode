#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 10:09
# @Author  : qkwu
# @File    : leetcode39CombinationSum.py

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        self.combine(results, [], candidates, target)
        return results



    def combine(self, results, result, candidates,target):
        if sum(result) == target:
            results.append(result)
            return
        elif sum(result) > target:
            return
        else:
            for i in range(len(candidates)):
                result.append(candidates[i])
                self.combine(results, result[:], candidates[i:], target)
                result.pop()



candidates = [2,3,5]
target = 8
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
sl = Solution()
print(sl.combinationSum(candidates, target))