# BOJ 11286 절댓값 힙

import heapq
import sys
input = sys.stdin.readline

N = int(input())
L = []

for i in range(N):
    n = int(input())
    if n: heapq.heappush(L, [abs(n), n])
    else:
        if not L: print(0)
        else: 
            a = heapq.heappop(L)
            print(a[1])