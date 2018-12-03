#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 15:30
# @Author  : qkwu
# @File    : leetcode25ReverseNodesinKGroups.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is
#not a multiple of k then left-out nodes in the end should remain as it is.

class Solution(object):
    def reverseKGroup(self, head, k):
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev

    def reverse(self, head, count):
        prev, cur = None, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)

def createLinkedList():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    return n1

if __name__ == '__main__':
    head = createLinkedList()
    sl = Solution()
    print(sl.reverseKGroup(head, 2).val)