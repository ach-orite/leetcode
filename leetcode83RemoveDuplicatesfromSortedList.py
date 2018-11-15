#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 11:28
# @Author  : qkwu
# @File    : leetcode83RemoveDuplicatesfromSortedList.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head.next
        slow = head
        while fast != None:
            if fast.val != slow.val:
                fast = fast.next
                slow = slow.next
            else:
                slow.next = fast.next
                fast = fast.next
        return head
