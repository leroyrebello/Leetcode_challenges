#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
567. Permutation in String
Medium
10.2K
328
Companies
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = Counter(s1)
        window = len(s1)

        for i in range (len(s2) - window + 1):
            s2count = Counter(s2[i:window + i])

            if s1count == s2count:
                return True
        return False














    

