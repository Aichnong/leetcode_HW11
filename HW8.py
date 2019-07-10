# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:52:09 2019

@author: user
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        c = len(nums);
        an = 0;
        for i in range(0,c,2):
            an = min(nums[i],nums[i+1])+an
        return an
s = Solution()
print(s.arrayPairSum([1,4,3,2]))