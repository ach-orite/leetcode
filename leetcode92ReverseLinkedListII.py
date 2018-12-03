#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 13:38
# @Author  : qkwu
# @File    : leetcode92ReverseLinkedListII.py

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None or head.next == None or m >= n or m < 0 or n < 0:
            return head
        dummyNode = ListNode(-1)
        dummyNode.next = head

        pre = dummyNode
        cur = head
        i = 1
        while i < m and cur != None:
            pre = cur
            cur = cur.next
            i += 1
        t1 = pre
        t2 = cur

        while i <= n and cur != None:
            lat = cur.next
            cur.next = pre
            pre = cur
            cur = lat
            i += 1
        t1.next = pre
        t2.next = cur

        return dummyNode.next

