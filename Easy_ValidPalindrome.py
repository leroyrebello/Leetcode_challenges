#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
125. Valid Palindrome
Easy
7.4K
7.4K
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newS = ''
        # for char in s:
        #     if char.isalnum():
        #         newS += char.lower()


        # return newS == newS[::-1]

        l = 0
        r = len(s)-1

        while l < r:
            while l < r and not self.alphanumeric(s[l]):
                l += 1
            while r > l and not self.alphanumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphanumeric (self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
            













    

