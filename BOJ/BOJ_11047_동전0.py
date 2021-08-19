# BOJ 11047 동전 0

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

ans = 0
for i in range(N - 1, -1, -1):
    ans += K // arr[i]
    K %= arr[i]

print(ans)    
