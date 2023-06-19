#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
961. N-Repeated Element in Size 2N Array
Easy
1.2K
318
Companies
You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

 

Example 1:

Input: nums = [1,2,3,3]
Output: 3
Example 2:

Input: nums = [2,1,2,5,3,2]
Output: 2
'''

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

       #Using set
        s = set()

        for n in nums:
            if n in s:
                return n
            else:
                s.add(n)    

        #Using Sort

        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]
   

