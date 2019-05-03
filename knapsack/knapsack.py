#!/usr/bin/python

import sys
import csv
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  total_weight = 0
  best = {'Value': 0, 'Chosen': []}
  for item in sorted(items, key=lambda i: i.value / i.size )[::-1]:
    index, weight, value = item
    if weight + total_weight <= capacity:
      best['Value'] += value
      best['Chosen'].append(index)
      total_weight += weight
  best['Chosen'].sort()
  return best
  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
