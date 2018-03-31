# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 20:17:42 2018

@author: lijie
"""

def Dijkstra_Arithmetic():
    node=find_lowest_cost_node(costs)
    while node is not None:
        cost=costs[node]
        neighbors=graph[node]
        #Traverse all the neighbors of the current node
        for n in neighbors.keys():
            new_cost=cost+neighbors[n]
            if costs[n]>new_cost:
                costs[n]=new_cost
                parents[n]=node
        processedNode.append(node)
        node=find_lowest_cost_node(costs)
    return new_cost
        
def find_lowest_cost_node(costs):
    lowest_cost=float('inf')
    lowest_cost_node=None
    for node in costs:
        cost=costs[node]
        if cost<lowest_cost and node not in processedNode:
            lowest_cost=cost
            lowest_cost_node=node
    return lowest_cost_node

        
            

if __name__=='__main__' :
    
    '''create a graph'''
    #graph is a hash table
    graph={}
    graph['start']={}
    graph['start']['a']=6
    graph['start']['b']=2
    #get all the neighbors of the beginning 'start'
    #print(graph['start'].keys())
    
    graph['a']={}
    graph['a']['fin']=1
    graph['b']={}
    graph['b']['a']=3
    graph['b']['fin']=5
    #the end point has no neighbors
    graph['fin']={}

    '''Create expense table'''
    #represent infinity
    infinity=float('inf')
    costs={}
    costs['a']=6
    costs['b']=2
    costs['fin']=infinity
        
    '''Create parent node table'''
    parents={}
    parents['a']='start'
    parents['b']='start'
    parents['fin']=None
    
    #create an array to store the node which we have processed
    processedNode=[]
    
    shortest_way=Dijkstra_Arithmetic()
    print(shortest_way)
    
    