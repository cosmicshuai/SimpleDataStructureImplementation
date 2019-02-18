# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 09:21:37 2019

@author: YS
"""
import math
class segmentTree:
    def __init__(self, nums: 'List[int]'):
        n = len(nums)
        power = math.ceil(math.log(n,2))
        total = 2**(power+1)
        self.__leaf_length = int(total/2)-1
        self.tree = [None]*total
        self.__build(0,0,self.__leaf_length,nums)

    def __left_child(self,root):
        return 2*root+1
    
    def __right_child(self,root):
        return 2*root+2

    def __build(self,node,l,r,nums):
        if l==r:
            self.tree[node]= 0
            try:
                self.tree[node]=nums[l]
            except IndexError:
                self.tree[node] = 0
            return 
        lc = self.__left_child(node)
        rc = self.__right_child(node)
        mid = (l+r)//2
        self.__build(lc,l,mid,nums)
        self.__build(rc,mid+1,r,nums)
        self.tree[node] = self.tree[lc]+self.tree[rc]
    
    def __update(self,node,l,r,i,val):
        if l==i and r==i:
            self.tree[node]=val
        elif i<l or i>r:
            return 
        else:
            lc = self.__left_child(node)
            rc = self.__right_child(node)
            mid = (l+r)//2
            self.__update(lc,l,mid,i,val)
            self.__update(rc,mid+1,r,i,val)
            self.tree[node] = self.tree[lc]+self.tree[rc]
    
    def update(self, i: 'int', val: 'int') -> 'None':
        self.__update(0,0,self.__leaf_length,i,val)

    def __query(self,node,l,r,i,j):
        if l>=i and r<=j:
            return self.tree[node]
        elif j<l or r<i:
            return None
        else:
            lc = self.__left_child(node)
            rc = self.__right_child(node)
            mid = (l+r)//2
            lr = self.__query(lc,l,mid,i,j)
            rr = self.__query(rc,mid+1,r,i,j)
            if lr and rr:
                return lr+rr
            elif lr and not rr:
                return lr
            elif not lr and rr:
                return rr
            else:
                return 0
            
    def query(self, i: 'int', j: 'int') -> 'int':
        return self.__query(0,0,self.__leaf_length,i,j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
        
nums = [4,1,3,5,11,6,9,2]
ob = segmentTree(nums)
print(ob.tree)
ob.update(3,10)
print(ob.tree)
print(ob.query(0,3))