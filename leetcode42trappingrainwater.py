#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 10:57
# @Author  : qkwu
# @File    : leetcode42trappingrainwater.py


#从最大值点把数组分成两部分，[begin，maxposition]闭区间，[maxposition，end]这个问题简化成一个问题，已知左/右边最高，求能接多少雨水？不失一般性，另右边最高，解左区间问题。单指针：
#试想，这时，任何一点 i 的水面高度一定一定一定是从【0，i】之间的最大值，和峰值max之间的最小值（这句话好好理解！！），这样问题就很简单了，从0开始遍历，一直更新我的leftmaxnum，如果需要更新，则这个点一定不存水，如果不更新，一定存leftmaxnum-height[i]高度的水，求和即可。


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxheight = max(height)
        pos = height.index(maxheight)
        res = 0
        leftmax = 0
        rightmax = 0
        for i in range(pos):
            if height[i] >= leftmax:
                leftmax = height[i]
            else:
                res += (leftmax - height[i])
        for i in range(len(height)-1, pos, -1):
            if height[i] >= rightmax:
                rightmax = height[i]
            else:
                res += (rightmax - height[i])
        return res



nums = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
sl = Solution()
print(sl.trap(height=nums))
