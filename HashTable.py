# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:14:07 2018

@author: lijie
"""

'''implementation of the hash table'''
#Method 1
a=dict()

#Method 2
b={}


'''implementation of cache using hash table'''
cache={}
def get_page(url):
    if cache.get(url):
        return chche[url]
    else:
        data=get_data_from_server(url)
        cache[url]=data
        return data