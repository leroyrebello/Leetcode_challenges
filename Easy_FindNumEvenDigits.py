#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
1295. Find Numbers with Even Number of Digits
Easy
2K
113
Companies
Given an array nums of integers, return how many of them contain an even number of digits.

 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
'''
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        res = 0
        for i in nums:
            if i > 9 and i <= 99:
                res += 1
            if i > 999 and i <= 9999:
                res += 1    
            if i > 99999 and i <= 999999:
                res += 1
        return res

