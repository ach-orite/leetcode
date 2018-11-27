#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 14:53
# @Author  : qkwu
# @File    : leetcode10RegularExpressionMatching.py

# 简单递归 超时
# class Solution(object):
#     def isMatch(self, s, p):
#         if not p: return not s
#         first_match = bool(s) and p[0] in [s[0],'.']
#
#         if len(p) >= 2 and p[1] == '*':
#             return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
#
#         return first_match and self.isMatch(s[1:], p[1:])

# DP
class Solution(object):
    def isMatch(self, s, p):
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].
        m, n = len(s) + 1, len(p) + 1
        matches = [[False] * n  for _ in range(m)]

        # Match empty string with empty pattern
        matches[0][0] = True

        # Match empty string with .*
        for i, element in enumerate(p[1:], 2):
            matches[0][i] = matches[0][i - 2] and element == '*'

        for i, ss in enumerate(s, 1):
            for j, pp in enumerate(p, 1):
                if pp != '*':
                    # The previous character has matched and the current one
                    # has to be matched. Two possible matches: the same or .
                    matches[i][j] = matches[i - 1][j - 1] and \
                                    (ss == pp or pp == '.')
                else:
                    # Horizontal look up [j - 2].
                    # Not use the character before *.
                    matches[i][j] |= matches[i][j - 2]

                    # Vertical look up [i - 1].
                    # Use at least one character before *.
                    #   p a b *
                    # s 1 0 0 0
                    # a 0 1 0 1
                    # b 0 0 1 1
                    # b 0 0 0 ?
                    # 因为j是从1开始enu,所以用p[j-2]实际上只是前一位，所以下式是为了尽量匹配更多的？*（如bbbbb 匹配b*）
                    if ss == p[j - 2] or p[j - 2] == '.':
                        matches[i][j] |= matches[i - 1][j]

        return matches[-1][-1]
s = "bbbacbcbcbbbbabbbab"
p = "b*c*c*.*.*.*ab*c"
# Output: true

sl = Solution()
print(sl.isMatch(s, p))

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# s = "aa"
# p = "a*"
# Output: true
#
#
# s = "aab"
# p = "c*a*b"
# Output: true
#
# s = "mississippi"
# p = "mis*is*p*."
# Output: false