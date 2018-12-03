#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 13:16
# @Author  : qkwu
# @File    : leetcode206ReverseLinkedList.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head

        while cur != None:
            lat = cur.next
            cur.next = pre
            pre = cur
            cur = lat

        return pre