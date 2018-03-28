# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:34:00 2018

@author: lijie
"""
from math import *

def binary_search(list,item):
    #list[low:high] is the interval which we shall search in
    #The index starts at 0. Namely,'1' is list_1[0]
    low=0
    high=len(list)-1
    while low<=high:
        mid=floor((low+high)/2)
        guess=list[mid]
        if guess==item:
            return mid
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    return None

#
if __name__=='__main__' :
    list_1=[1,3,5,7,9]
    
    a=binary_search(list_1,3)
    b=binary_search(list_1,2)
    print(a,b)