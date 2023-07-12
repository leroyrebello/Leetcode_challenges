#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
234. Palindrome Linked List
Easy
14.5K
797
Companies
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''Using Arrays'''
        res = []

        while head:
            res.append(head.val)
            head = head.next

        l , r = 0 , len(res) -1
        while l <= r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True

    '''Using LL'''
# mid, end = head, head

#         # find mid
#         while end and end.next:
#             end = end.next.next
#             mid = mid.next
#         #reverse 2nd half of LL
#         prev = None
#         while mid:
#             tmp = mid.next
#             mid.next = prev
#             prev = mid
#             mid = tmp

#         #actual checking
#         l, r = head, prev
#         while r:
#             if l.val != r.val:
#                 return False
#             l = l.next
#             r = r.next
#         return True
            

        


    

