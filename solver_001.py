#!/usr/bin/python
# -*- coding: utf-8 -*-
# greedy by value
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
    
    items.sort(key= lambda items: items.value // items.weight)
    print('003 items \n', items)
    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    print('start')
    file_location = "path_to_files" #ks_19_0, ks_30_0, ks_300_0
    with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
            print('----final---',solve_it(input_data))
    
'''
metrix greedy vs dynamic
ks_19 : 11476 vs 12248
ks_30 : 90,000 vs 99798

'''

