# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 20:12:34 2018

@author: lijie
"""
from collections import deque

def bfs_ergodic(name):
    
    '''create a queue using the graph'''
    search_queue=deque()
    search_queue+=graph[name]
    searched=[]
    
    '''bfs implementation'''
    while search_queue:
        #pop the first persoon in the queue
        person=search_queue.popleft()
        #Skip the people we have checked
        if not person in searched:
            if name_ended_m(person):
                print(person,'is~')
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False


#judge if a person's name is ended with 'm'
def name_ended_m(person):
    return person[-1]=='m'
    
if __name__=='__main__' :
    
    '''create a graph'''
    #graph is a hash table
    graph={}
    graph['you']=['alice','bob','claire']
    graph['alice']=['peggy']
    graph['bob']=['anuj','peggy']
    graph['claire']=['tomm','jonny']
    graph['anuj']=[]
    graph['peggy']=[]
    graph['tomm']=[]
    graph['jonny']=[]
    
    bfs_ergodic('you') 