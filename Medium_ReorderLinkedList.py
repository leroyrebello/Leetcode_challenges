#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
143. Reorder List
Medium
9.1K
302
Companies
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        '''to find mid and end'''
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        '''reverse 2nd half of LL'''
        prev = None
        head2 = slow.next #head of 2nd List
        while head2:
            temp = head2.next
            head2.next = prev 
            prev = head2 #move prev to next node
            head2 = temp  #move head2 to next node 
        slow.next = None #Whyy? because slow=4 and slow.next is pointing to 5. but we need to break the connection so slow.next = Null. So now 1,2,3,4 is list1 and 7,6,5 is list2.
        
        '''Actual logic'''
        head1, head2 = head, prev
        while head2:
            temp1, temp2 = head1.next, head2.next
            head1.next = head2
            head2.next = temp1
            head1, head2 = temp1, temp2 #appending head1 and head2 to next node.
        














    

