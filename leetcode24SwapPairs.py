#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 17:01
# @Author  : qkwu
# @File    : leetcode24SwapPairs.py

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        new_head = head.next
        next_head = new_head.next

        new_head.next = head
        head.next = self.swapPairs(next_head)
        return new_head
