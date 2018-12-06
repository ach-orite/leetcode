#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 10:09
# @Author  : qkwu
# @File    : leetcode40CombinationSumII.py

#   Runtime: 1492 ms, faster than 1.03% of Python3 online submissions for Combination Sum II.
# class Solution:
#     def combinationSum2(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         candidates.sort()
#         results = set()
#         self.combine(results, [], candidates, target)
#         results1 = []
#         for st in results:
#             results1.append(list(st))
#         return results1
#
#     def combine(self, results, result, candidates, target):
#         if sum(result) == target:
#             results.add(tuple(result))
#             return
#         elif sum(result) > target:
#             return
#         else:
#             for i in range(len(candidates)):
#                 result.append(candidates[i])
#                 self.combine(results, result[:], candidates[i+1:], target)
#                 result.pop()


class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return  # backtracking
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)



candidates = [15,20,11,26,13,30,31,27,8,27,6,28,22,12,17,9,8,21,12,21,15,25,7,23,15,23,24,28,28,17,11,30,24,9,13,33,26,10,25,22,24,27,15,11,34,19,15,29,6,14,15,8,5,9,18,15,28,30,9,13,34,7,30]
target = 28
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

sl = Solution()
print(sl.combinationSum2(candidates, target))
