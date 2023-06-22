#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
58. Length of Last Word
Easy
3.4K
180
Companies
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count = 0
        for i in range(len(s)-1,-1,-1):
            if (s[i] >= chr(97) and s[i] <= chr(122)) or (s[i] >= chr(65) and s[i] <= chr(90)):
                count+=1
            if s[i] == ' ' and count == 0:
                continue   
            elif s[i] == ' ' and count > 0:
                return count
        return count

