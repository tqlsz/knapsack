#!/usr/bin/python
# -*- coding: utf-8 -*-
import knapsack
import gc
import sys
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])
sys.setrecursionlimit(1500)
def solve_it(input_data):
    # Modify this code to run your optimization algorithm
    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full

    value = 0

    # weight = 0

    taken = [0]*len(items)
    # print taken, item_count
    # ******
    j = item_count
    root = knapsack.Node(0, 0, capacity)
    tree = knapsack.Optimal_dps_tree(root, capacity,\
            [x[2] for x in items], [x[1] for x in items])
    tree.recur_create_preorder(tree.root)
    value = int(tree.maxV)
    for el in tree.max_index:
        taken[int(el)] = 1

    '''
    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    '''
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

