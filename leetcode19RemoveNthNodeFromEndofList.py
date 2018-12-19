#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:38
# @Author  : qkwu
# @File    : leetcode19RemoveNthNodeFromEndofList.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        slow = head
        for _ in range(n):
            if fast.next != None:
                fast = fast.next
            else:
                head = head.next
                return head
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head
