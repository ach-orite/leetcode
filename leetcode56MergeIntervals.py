#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 14:12
# @Author  : qkwu
# @File    : leetcode56MergeIntervals.py

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        intervals.sort(key = lambda interval : interval.start)
        stack = [intervals[0]]
        for interval in intervals[1:]:
            if stack[-1].end >= interval.start:
                if stack[-1].end < interval.end:
                    stack[-1].end = interval.end
            else:
                stack.append(interval)

        return stack

