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

  # passes the tests
  # """
  # Correct but very memory inefficient solution, can only solve problems where
  # computer memory is at least number of items times capacity time 8bytes large
  # """
  # # Initialize the cache matrix: rows are items (including a "no item" row)
  # # Columns are integral capacities: 0, 1, 2, ..., capacity - 1, capacity
  # cache = [[0] * (capacity + 1) for _ in range(len(items) + 1)]

  # # Our bag represented as a Set data structure
  # bag = set()

  # # DP loops for filling in cache matrix
  # # if the item does not fit in a "sub-knapsack", don't include it
  # # else include it only if its value makes the knapsack more valuable
  # # These loops fill the matrix but do not solve the problem
  # # Note - first row is all 0s because picking from 0 items
  # # Need to have it to refer back to for solution computation
  # for item in range(1, len(cache)):
  #   for size in range(len(cache[item])):
  #     if items[item-1].size > size:
  #       # Item doesn't fit, skip
  #       cache[item][size] = cache[item-1][size]
  #     else:
  #         # Item fits, take max of skipping it or adding it
  #         # Adding -> base new knapsack on current - size + value of item
  #       cache[item][size] = max(
  #         cache[item-1][size],
  #         cache[item-1][size - items[item-1].size] + items[item-1].value)

  # # With this loop we can traverse the matrix and figure out what items
  # # to take in our knapsack, that is, if the value increased from item i-1
  # # to item i then we know we took the item and should go to the previous
  # # item in the smaller knapsack
  # # (the column discounting the size of the taken item)
  # rows = len(cache) - 1
  # cols = len(cache[-1]) - 1
  # while rows > 0 and cols > 0:
  #   if cache[rows][cols] != cache[rows-1][cols]:
  #     bag.add(rows - 1)
  #     rows -= 1
  #     cols -= items[rows].size
  #   else:
  #     rows -= 1

  # return dict(Value=cache[-1][-1], Chosen=list(sorted(map(lambda i: i+1, bag))))
  

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
