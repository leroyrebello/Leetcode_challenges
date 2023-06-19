#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
Easy_LargestUniqueNumber
Given an array of integers A, return the largest integer that only occurs once.
If no integer occurs once, return -1.

 

Example 1:

Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: 
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.
'''

class Solution:
    def LargestUniqueNum(self, nums: List[int]) -> int:
        
        nums = sorted(nums, reverse = True)
        
        for i in nums:
            if i != i+1 and i+1 != i+2:
                return i+1
        return -1
   
   


# In[ ]:




