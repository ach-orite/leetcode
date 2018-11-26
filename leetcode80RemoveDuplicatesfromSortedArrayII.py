#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 10:28
# @Author  : qkwu
# @File    : leetcode80RemoveDuplicatesfromSortedArrayII.py

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3: return len(nums)

        # 维护2个两个指针和一个变量d
        d = 1
        result = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                d = 1
                nums[result]=nums[i]
                result += 1
            else:
                if (d < 2):
                    d += 1
                    nums[result]=nums[i]
                    result += 1
        return result

        #用list.pop()方法
        # i = 2
        # while i < len(nums):
        #     if nums[i] == nums[i - 1] and nums[i - 1] == nums[i - 2]:
        #         nums.pop(i)
        #     else:
        #         i += 1
        # return len(nums)

nums = [0,0,1,1,1,1,2,3,3]
# return 7
sl = Solution()
print(sl.removeDuplicates(nums))