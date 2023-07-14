#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
20. Valid Parentheses
Easy
20.8K
1.3K
Companies
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''
class Solution:
    def isValid(self, s: str) -> bool:
        ClosetoOpen = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for i in s:
            if i in ClosetoOpen: #checking until we get a closing parentheses in s
                if stack and stack[-1] == ClosetoOpen[i]: #checking if stack is empty #and checking if the last item in stack is matching with the hashmap
                    stack.pop()  #pop the last element i.e. opening parenthesis
                else:
                    return False   
            else:
                stack.append(i)
        
        return True if not stack else False














    

