# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:43:35 2019

@author: user
"""

class Solution(object):
    def numJewelsInStones(self, J, S):
        array=[]
        for i in list(S):
            if i in list(J):
                array.append(i)
        return len(array)