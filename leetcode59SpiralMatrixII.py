#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 17:07
# @Author  : qkwu
# @File    : leetcode59SpiralMatrixII.py

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return list()
        matrix = [[1] * n for x in range(n)]
        print(matrix)

        rowstart = 0
        rowend = n - 1
        columnstart = 0
        columnend = n - 1
        count = 1
        while rowstart <= rowend and columnstart <= columnend:
            if rowstart < rowend and columnstart < columnend:
                for i in range(columnstart, columnend + 1):
                    matrix[rowstart][i] = count
                    count += 1
                for i in range(rowstart + 1, rowend + 1):
                    matrix[i][columnend] = count
                    count += 1
                for i in range(columnend - 1, columnstart, -1):
                    matrix[rowend][i] = count
                    count += 1
                for i in range(rowend, rowstart, -1):
                    matrix[i][columnstart] = count
                    count += 1
            elif rowstart == rowend and columnstart < columnend:
                for i in range(columnstart, columnend + 1):
                    matrix[rowstart][i] = count
                    count += 1
                return matrix
            elif rowstart < rowend and columnstart == columnend:
                for i in range(rowstart, rowend + 1):
                    matrix[i][columnstart] = count
                count += 1
                return matrix
            elif rowstart == rowend and columnstart == columnend:
                matrix[rowstart][columnend] = count
                count += 1
                return matrix
            rowstart += 1
            rowend -= 1
            columnstart += 1
            columnend -= 1
        return matrix




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
print(sl.generateMatrix(3))