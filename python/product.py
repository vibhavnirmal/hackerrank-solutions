#https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

pq=[]
for i in product(A,B):
    pq.append(i)

print(*pq)