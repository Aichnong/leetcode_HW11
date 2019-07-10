# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:49:10 2019

@author: user
"""

class Solution(object):
    def flipAndInvertImage(self, A):
        a=[]
        b=[]
        for i in range(len(A)):
            a=A[i]
            a.reverse()
            b.append(a)
            for j in range(len(A[0])):
                if(b[i][j]==1):
                    b[i][j]=0
                else:
                    b[i][j]=1
        return b
s = Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))