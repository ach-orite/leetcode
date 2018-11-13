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
        if not nums1 or not nums2:
            nums1 = nums1 + nums2
        else:
            cur = 0
            p1 = 0
            p2 = 0
            while cur < m and p2 < n:
                if nums1[p1] <= nums2[p2]:
                    cur += 1
                    p1 += 1
                else:
                    p1 += 1
                    nums1[p1:] = nums1[p1-1:-1]
                    nums1[p1-1] = nums2[p2]
                    p2 += 1
            if p2 < n:
                nums1[-(n-p2):] = nums2[p2:]



nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5, 6]
n = 5

sl = Solution()
print(sl.merge(nums1, m, nums2, n))
print(nums1)