#https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

M = list(input().split())
for i in range(1, int(M[1])+1):
    for j in combinations(sorted(M[0]),i):
        print(''.join(j))