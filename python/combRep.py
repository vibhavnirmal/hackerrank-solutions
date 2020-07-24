# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

M, num = input().split()
num = int(num)
f = list(combinations_with_replacement(sorted(M),num))
for i in f:
    print(''.join(i))