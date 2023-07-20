#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
2405. Optimal Partition of String
Medium
2.2K
84
Companies
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

 

Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
'''
class Solution:
    def partitionString(self, s: str) -> int:
        set1 = set()

        res = 1   #start from 1 because we will have atleast 1 string

        for i in s:
            if i in set1:   #checking in char is in the hashset
                res += 1       #if yes update res
                set1 = set()     #and reset hashset
            set1.add(i)     #if not in hashset, we add the new char to the set
        return res












    

