# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:42:52 2019

@author: user
"""

class Solution(object):
    def defangIPaddr(self, a):
        """
        :type address: str
        :rtype: str
        """
        return a.replace('.','[.]')
s = Solution()
print(s.defangIPaddr("1.1.1.1"))