#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 16:57
# @Author  : qkwu
# @File    : leetcode93RestoreIPAddress.py

# 本题回溯法，特色主要是使用了一个cur数组 来判断当前的path是否满足要求
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if len(s) > (4 - len(path)) * 3:
            return
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        for i in range(min(3, len(s))):
            curr = s[:i + 1]
            if (curr[0] == '0' and len(curr) >= 2) or int(curr) > 255:
                continue
            self.dfs(s[i + 1:], path + [s[:i + 1]], res)


str = "25525511135"
#Output: ["255.255.11.135", "255.255.111.35"]
sl = Solution()
print(sl.restoreIpAddresses(str))