#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    print('001', input_data)
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)
    '''[Item(index=0, value=8, weight=4), Item(index=1, value=10, weight=5), Item(index=2, value=15, weight=8), Item(index=3, value=4, weight=3)]'''
    #print('002 items \n', items[0].index == 0, items[0].value)

    
    # create table
    table = {(x,y):0 for x in range(capacity+1) for y in range(item_count)} # dict for lookup
    #print(table)
    
    # fill table
    for y in table: #(11, 3) ( current capacity, item index)
        #print('003', items[y[1]], y)    
        current_i = items[y[1]]
        current_v, current_w = current_i.value, current_i.weight
        
        if y[0] != 0:
            z = y[0] - current_w
            #print('--z--', z )
            if z == 0: table[y] = current_v
            elif z > 0: # there's space. z is the additional capacity
                if 0 not in y:  #(11, 3) ( current capacity, item index)
                    a1 = table[(y[0],y[1]-1)] # take previous item
                    a2 = table[(z,y[1]-1)] + current_v
                    
                    table[y] = max(a1,a2)
                
                if y[1] == 0:
                    a3 = current_v
                    a4 = table[(z,0)]
                    table[y] = max(a3,a4)

            elif z < 0: # there is no space for this item
                if y[1] != 0:
                    table[y] = table[(y[0],y[1]-1)]
                if y[1] == 0:
                    a4 = table[(y[0] -1 ,0)]
                    table[y] = a4

                        
            #print('004', table[y],z) 

    #print(table)
    
    #read table
    xyz = [capacity, item_count - 1]
    picked = [0] * item_count
    i = len(table)
    #print('006', xyz, picked)
    while i > 0:
        current_i = items[xyz[1]]
        if table[(xyz[0],xyz[1])] != table[(xyz[0] -1 ,xyz[1]-1)]:

            picked[xyz[1]] = 1
            xyz[0] =  xyz[0] - current_i.weight
            xyz[1] = xyz[1]-1

            if table[(xyz[0] ,xyz[1])] == 0:
                break
    
        if table[(xyz[0],xyz[1])] == table[(xyz[0] -1 ,xyz[1]-1)]:
            xyz[1] = xyz[1]-1

        i = i - 1
    print(picked, capacity)
    value = table[(capacity, item_count - 1)]
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, picked))
    return output_data


if __name__ == '__main__':
    import sys, time
    print('start')
    file_location = "path_to_files" # ks_19_0, ks_4_0, ks_30_0
    with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
            print('----final---',solve_it(input_data))
    
    
