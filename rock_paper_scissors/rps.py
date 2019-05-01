#!/usr/bin/python

import sys

def rock_paper_scissors(n, moves=[[[]]]):
  if n < 0:
    return []
  rps = ['rock', 'paper', 'scissors']
  
  for i in range(1, n+1):
    last_entry = moves[i-1]
    moves.append([])
    for j in range(len(last_entry)):
      last_moves = last_entry[j]
      for move in rps:
        moves[i].append(last_moves + [move])

  return moves[n]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
    print('Here is an example using 2, as in rps.py 2')
    cache = [[], rock_paper_scissors(1)]
    print(rock_paper_scissors(2, cache))
