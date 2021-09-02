# BOJ 11279 최대 힙

import heapq
import sys
input = sys.stdin.readline

N = int(input())
L = []
for i in range(N):
    n = int(input())
    if n: heapq.heappush(L, -n)
    else:
        if not L: print(0)
        else: print(-heapq.heappop(L))
