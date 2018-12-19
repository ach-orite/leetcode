#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:37
# @Author  : qkwu
# @File    : leetcode17LetterCombinationsOfAPhoneNumber.py

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        maps = {1: '*', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        return list(map(lambda x: "".join(x), itertools.product(*[maps[int(d)] for d in digits])))
