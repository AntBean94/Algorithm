# BOJ 10773 제로

import sys
input = sys.stdin.readline

stack = []
total = 0
K = int(input())
for k in range(K):
    n = int(input())
    if n: 
        stack.append(n)
        total += n
    else:
        m = stack.pop()
        total -= m
print(total)