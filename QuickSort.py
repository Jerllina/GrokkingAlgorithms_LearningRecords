# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 15:31:06 2018

@author: lijie
"""
from numpy import *

'''the recursion version of quicksort'''
def quicksort_recursion(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        smaller=[i for i in array[1:] if i<=pivot]
        greater=[i for i in array[1:] if i>pivot]
        return(quicksort(smaller)+[pivot]+quicksort(greater))

'''the circulation version of quicksort'''
def quicksort_circulation(array):
    smaller=[]
    greater=[]
    if len(array)<2:
        return array
    else:              
        for i in range(1,(len(array))):
            pivot=array[0]
            if array[i]<=pivot:
                smaller.append(array[i])
            else:
                greater.append(array[i])
                
        return(quicksort(smaller)+[pivot]+quicksort(greater))
   
    
#test
array1=array([10,5,3,1,5])
print('the the recursion version of quicksort of this array is :\t',quicksort_recursion(array1))
print('the the circulation version of quicksort of this array is :\t',quicksort_circulation(array1))