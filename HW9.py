# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:52:39 2019

@author: user
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for key in nums:
            dict[key] = dict.get(key, 0) + 1
        num = [x for x, y in dict.items() if y == 1]
        return num[0]
s = Solution()
print(s.singleNumber([2,2,1]))