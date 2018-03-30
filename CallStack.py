# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:23:31 2018

@author: lijie
"""
#Function stack
def greet(name):
    print('hello,',name,'!')
    greet2(name)
    print('getting ready to say good bye')
    bye()
    
def greet2(name):
    print('how are you,',name,'?')

def bye():
    print('ok bye!')

#Recursion  stack ( factorial example 求阶乘)
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
       
if __name__=='__main__' :

    greet('jelina')
    print('the factorial of 5 is:',fact(5))