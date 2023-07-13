#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
19. Remove Nth Node From End of List
Medium
16.3K
675
Companies
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(next = head)
        first, second = dummy, head

        while n > 0:
            second = second.next
            n -= 1
        
        while second:
            first = first.next
            second = second.next
        first.next = first.next.next

        return dummy.next

        














    

