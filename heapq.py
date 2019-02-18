# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:17:47 2019

@author: cosmic
"""

class Myheap(object):
    def __init__(self):
        self.data = []
        
    def size(self):
        return len(self.data)
    
    def left_child(self,root):
        return 2*root+1
    
    def right_child(self,root):
        return 2*root+2
    
    def parent(self,child):
        if child == 0:
            return 0
        return (child-1)//2
    
    def heapnify(self,root):
        if root>=self.size():
            return
        lc = self.left_child(root)
        rc = self.right_child(root)
        largest = root
        if lc<self.size():
            if self.data[lc]>self.data[largest]:
                largest = lc
        if rc<self.size():
            if self.data[rc]>self.data[largest]:
                largest = rc
        if largest != root:
            self.data[root], self.data[largest] = self.data[largest], self.data[root]
            self.heapnify(largest)
            
    def build_heap(self):
        for i in range(self.size()//2,-1,-1):
            self.heapnify(i)
    
    def push(self,val):
        self.data.append(val)
        index = self.size()-1
        root = self.parent(index)        
        while self.data[root]<self.data[index]:
            self.data[root],self.data[index] = self.data[index],self.data[root]
            index = root
            root = self.parent(index)
    def pop(self):
        if self.size()<0:
            return None
        val = self.data.pop(0)
        print(self.data)
        self.heapnify(0)
        return val
        
h = Myheap()
h.data = [1,6,5,8,2,7,4]
h.build_heap()
print(h.data)
print(h.pop())
print(h.data)
