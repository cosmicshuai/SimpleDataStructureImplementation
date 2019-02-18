# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 13:51:27 2019

@author: cosmic
"""

class BITree:
    def __init__(self,nums):
        n = len(nums)
        self.bit = [0]*(n+1)
        print(self.bit)
        self.n = n
        for i in range(n):
            self.__update(self.bit,n,i,nums[i])
    
    def __update(self,bit,n,i,v):
        i += 1
        while i<=n:
            bit[i] += v
            i += i & (-i)
    
    def update(self,i,v):
        #add v to nums[i]
        self.__update(self.bit,self.n,i,v)
        
    def __query(self,bit,i):
        s = 0
        i += 1
        while i>0:
            s += bit[i]
            i -= i&(-i)
        return s
    
    def query(self,i):
        assert i<self.n
        return self.__query(self.bit,i)
        
            
nums = [4,5,1,3,7,2,6]
ob = BITree(nums)
print(ob.bit)
#ob.update(0,5)
#print(ob.bit)
print(ob.query(3))