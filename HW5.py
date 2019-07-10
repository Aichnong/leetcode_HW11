# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:49:39 2019

@author: user
"""

class Solution:
    def sortArrayByParity(self, A):
        a = []
        b = []
        for i in A:
            if (i % 2) == 0:
                a.append(i)
            else:
                b.append(i)
        return a+b
s = Solution()
print(s.sortArrayByParity([3,1,2,4]))