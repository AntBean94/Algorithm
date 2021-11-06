# BOJ 9084 동전

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    DP = [0] * (M + 1)
    for c in coin:
        for i in range(M + 1):
            t = i - c
            if t == 0: DP[i] += 1
            if t > 0: DP[i] += DP[i - c]
    print(DP[M])
