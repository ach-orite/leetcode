#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 13:57
# @Author  : qkwu
# @File    : leetcode54SpiralMatrix.py

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res + matrix
        else:
            rowstart = 0
            rowend = len(matrix) - 1
            columnstart = 0
            columnend = len(matrix[0]) - 1
            while rowstart <= rowend and columnstart <= columnend:
                if rowstart < rowend and columnstart < columnend:
                    for i in range(columnstart, columnend + 1):
                        res.append(matrix[rowstart][i])
                    for i in range(rowstart + 1, rowend + 1):
                        res.append(matrix[i][columnend])
                    for i in range(columnend - 1, columnstart, -1):
                        res.append(matrix[rowend][i])
                    for i in range(rowend, rowstart, -1):
                        res.append(matrix[i][columnstart])
                elif rowstart == rowend and columnstart < columnend:
                    for i in range(columnstart, columnend + 1):
                        res.append(matrix[rowstart][i])
                    return res
                elif rowstart < rowend and columnstart == columnend:
                    for i in range(rowstart, rowend + 1):
                        res.append(matrix[i][columnstart])
                    return res
                elif rowstart == rowend and columnstart == columnend:
                    res.append(matrix[rowstart][columnend])
                    return res
                rowstart += 1
                rowend -= 1
                columnstart += 1
                columnend -= 1
            return res


Input = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Input2 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [9,10,11,12],
  [9,10,11,12]
]
input = [
  [3],
  [5]
]
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]

sl = Solution()
print(sl.spiralOrder(Input))