#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
83. Remove Duplicates from Sorted List
Easy
7.6K
254
Companies
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        curr = head


        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next


            curr = curr.next
                 
           
        return head



    

