# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:22:00 2018

@author: lijie

"""

#find the smallest number
def findSmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

#the selection sort algorithm
def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest=findSmallest(arr)
        #pop() used to remove an element from the list
        newArr.append(arr.pop(smallest))
    return newArr

#test
print(selectionSort([5,3,1,6,2,10]))