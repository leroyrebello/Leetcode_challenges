#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
605. Can Place Flowers
Easy
5.2K
878
Companies
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        f = [0] + flowerbed + [0]
        if n == 0:
            return True
        for i in range(1,len(f)-1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                n -= 1 
                f[i] = 1
        return True if n <= 0 else False
            
    
    

