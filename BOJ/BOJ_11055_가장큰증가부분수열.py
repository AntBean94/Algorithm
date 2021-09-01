# BOJ 11055 가장 큰 증가 부분 수열

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

table = [0] * 1001

for i in range(N):
    n = arr[i]
    table[n] = max(table[:n]) + n
print(max(table))