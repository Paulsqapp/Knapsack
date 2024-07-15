#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from queue import PriorityQueue

Item = namedtuple("Item", ['index', 'value', 'weight'])
branch = namedtuple("branch", ['value','weight','estimate', 'path', ]) # sack_value, weight, extimate, apth

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    #print('001', input_data)
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    max_estimate = 0

    items = []
    items_sort = PriorityQueue()

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        max_estimate += int(parts[0])
        items.append(Item(i-1, int(parts[0]), int(parts[1]), ))
    
    # sack_value, weight, extimate, apth
    items_sort.put((-max_estimate,branch(0, capacity, max_estimate, [] ))) # use -ve numbers to do sorting

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    #x = items_sort.get() #  (-2.0, Item(index=0, value=8, weight=4))
    #x2 = items_sort.get() # (-1.875, Item(index=2, value=15, weight=8))
    #x3 = items_sort.get() # (-1.3333333333333333, Item(index=3, value=4, weight=3)
    
    '''[Item(index=0, value=8, weight=4), Item(index=1, value=10, weight=5), Item(index=2, value=15, weight=8), Item(index=3, value=4, weight=3)]'''
    #print('002 items \n',max_estimate, item_count)

    index, best_estimate, val_ = 0, 0, []
    x = item_count
    while not items_sort.empty():
        #print('start here \n')
        node = items_sort.get() # (-37, branch(value=0, weight=19, estimate=37, path=[])) 
        #print('\n start here node', node, len(node[1][-1]), '\n')

        if len(node[1][-1]) <= items[-1][0]:
            current_item = items[len(node[1][-1])] #  Item(index=0, value=8, weight=4)

            # take item sack_value, weight, extimate, apth, 
            #items_sort.put((-max_estimate,branch(0, 0, max_estimate, [] )))

            if node[1][1] - current_item[2] >= 0: #weight constraint
                
                sack_v = node[1][0] + current_item[1]
                
                rem_weight = node[1][1] - current_item[2]
                path_ = node[1][-1] +[ 1 ]
                items_sort.put(( -max_estimate, branch(sack_v, rem_weight,node[1][2], path_  )))
                #print('here------------', ( -max_estimate, branch(sack_v, rem_weight,node[1][2], path_  )))
            
            # dont take item
            sack_v2 = node[1][0]
            rem_weight_2 = node[1][1]
            path_2 = node[1][-1] +[0] # no item is taken
            max_estimate_2 = node[1][2] - current_item[1]
            
            items_sort.put(( -max_estimate_2, branch(sack_v2, rem_weight_2,max_estimate_2, path_2  )))
            #print('here------------2 ', ( -max_estimate_2, branch(sack_v2, rem_weight_2,max_estimate_2, path_2  )))

        #print('best estimate', best_estimate, node[1][0])
        if node[1][0] >= best_estimate:
            best_estimate = node[1][0]
            #print('best estimate', best_estimate, node[1][0])
            val_ = node



        #print('node',node, '\n item', current_item)
        
        index += 1
        x = x- 1

    #print('val -- ',val_)
    
    #print(picked, capacity)
    value = val_[1][0]
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, val_[1][3]))
    return output_data


if __name__ == '__main__':
    import sys, time
    #print('start') #"C:\Users\paul kuria\Documents\knapsack\data\ks_30_0"
    file_location = "C:/Users/paul kuria/Documents/knapsack/data/ks_82_0" # ks_19_0, ks_4_0, ks_30_0
    with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
            print('----final---',solve_it(input_data))
    
    
