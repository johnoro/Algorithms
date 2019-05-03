#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=[]):
  if n < 0:
    return eating_cookies(abs(n))
  ways = [1, 1, 2]
  i = curr = len(ways) - 1
  if n <= i:
    return ways[n]
  while curr < n:
    a, b, c = ways
    ways[i] += a+b
    ways[i-1] = c
    ways[i-2] = b
    curr += 1
  return ways[i]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
