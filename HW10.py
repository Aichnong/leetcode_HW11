# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:53:14 2019

@author: user
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]
    
s = Solution()
print(s.majorityElement([3,2,3]))