# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 16:47:40 2018

@author: lijie
"""

'''Set coverage problem / Greedy Algorithm'''
def choose_best_station():
    states_needed=statesneeded
    while states_needed:
        
        best_station=None
        states_covered=set()
        #traverse all stations
        for station,states_for_station in stations.items():
            covered=states_needed & states_for_station
            if len(covered)>len(states_covered):
                best_station=station
                states_covered=covered
        
        final_stations.add(best_station)
        states_needed-=states_covered
        
    print(final_stations)

if __name__=='__main__' :
    
    '''input the list & translate into a set'''
    statesneeded=set(['mt','wa','or','id','nv','ut','ca','az'])
    
    final_stations=set()    
    
    '''store the information into a hash table'''
    stations={}
    stations['kone']=set(['id','nv','ut'])
    stations['ktwo']=set(['wa','id','mt'])
    stations['kthree']=set(['or','nv','ca'])
    stations['kfour']=set(['nv','ut'])
    stations['kfive']=set(['ca','az'])
    
    choose_best_station()
    

    
