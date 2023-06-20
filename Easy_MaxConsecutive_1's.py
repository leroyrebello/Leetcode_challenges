#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
485. Max Consecutive Ones
Easy
4.5K
432
Companies
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
                res = max(res, temp)
            else: 
                temp = 0
                
        return res

