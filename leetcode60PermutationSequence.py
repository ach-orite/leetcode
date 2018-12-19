#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 9:38
# @Author  : qkwu
# @File    : leetcode60PermutationSequence.py

# 使用老的递归求下一个permutation k次方法 超时，只能通过分析结果来找规律

import math

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        numbers = [str(i) for i in range(1, n+1)]
        print(numbers)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation

    # def getPermutation(self, n, k):
    #     numbers = [str(i) for i in range(1, n + 1)]
    #     print(numbers)
    #     count = 1
    #     while count < k:
    #         numbers = self.nextPermutation(numbers)
    #         count += 1
    #     return ''.join(numbers)
    #
    #
    #
    # def nextPermutation(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     length = len(nums)
    #     for i in range(length - 2, -1, -1):
    #         if nums[i] < nums[i + 1]:
    #             for k in range(length - 1, -1, -1):
    #                 if nums[k] > nums[i]:
    #                     nums[i], nums[k] = nums[k], nums[i]
    #                     nums[i+1:] = sorted(nums[i+1:])
    #                     return nums
    #     return nums


n = 4
k = 9
#Output: "2314"

sl = Solution()
print(sl.getPermutation(4, 9))