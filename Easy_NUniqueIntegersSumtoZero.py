#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
1304. Find N Unique Integers Sum up to Zero
Easy
1.7K
560
Companies
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
'''

class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        i = 1
        res = []

        if n%2 == 0:
            while len(res) < n:
                res.append(i)
                res.append(i*(-1))
                i+=1
            return res    
        else:
            res.append(0)
            while len(res) < n:
                res.append(i)
                res.append(i*(-1))
                i+=1
            return res 
   


# In[ ]:




