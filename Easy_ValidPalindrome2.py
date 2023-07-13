#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
680. Valid Palindrome II
Easy
7.4K
378
Companies
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                if skipL == skipL[::-1] or skipR == skipR[::-1]:
                    return True
                else:
                    return False
            l += 1
            r -= 1
        return True













    

