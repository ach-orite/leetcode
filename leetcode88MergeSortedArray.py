#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 16:41
# @Author  : qkwu
# @File    : leetcode88MergeSortedArray.py

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for _ in range(m + n):
            cur = 0
            idx1 = 0
            idx2 = 0
            if nums1[idx1] <= nums2[idx2]:
                idx1 += 1
                cur += 1
            else:
                nums1[cur:] = nums2[idx2]+nums1[cur+1:-1]
                idx2 += 1
                cur += 1

        return nums1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

sl = Solution()
print(sl.merge(nums1, m, nums2, n))