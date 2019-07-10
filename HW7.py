# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:51:02 2019

@author: user
"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ai = []
        for i in range(left, right+1):
            for g in str(i):
                if g == '0' or i % int(g)!=0:
                    break
            else:
                ai.append(i)
        return ai
        
s = Solution()
print(s.selfDividingNumbers(1,22))