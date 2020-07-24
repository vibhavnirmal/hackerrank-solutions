#https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

M = list(input().split())
pp = list(permutations(M[0],int(M[1])))
pp.sort()
for i in pp:
    print ("".join(i))