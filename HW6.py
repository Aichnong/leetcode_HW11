# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:50:28 2019

@author: user
"""

class Solution(object):
    def sortedSquares(self, A: List[int]) -> List[int]:
        new_list =[n*n for n in A]
        return sorted(new_list)
s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))