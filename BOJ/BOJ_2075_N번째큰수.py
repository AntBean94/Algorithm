# BOJ 2075 N번째 큰 수

import sys
input = sys.stdin.readline
import heapq

N = int(input())
Q = []
for i in range(N):
    arr = list(map(int, input().split()))
    for a in arr:
        heapq.heappush(Q, a)
    if i == 0: continue
    for n in range(N):
        heapq.heappop(Q)
print(heapq.heappop(Q))