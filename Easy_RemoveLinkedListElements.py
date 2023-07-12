#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
203. Remove Linked List Elements
Easy
7.5K
211
Companies
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
'''
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(next = head)
        prev = dummy
       
        while curr:
            if curr.val == val:
                print("we are here", curr.val)
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
        


    

