# BOJ 14002 가장 긴 증가하는 부분 수열 4

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

table = [0] * 1001
route = ['0'] * 1001

for i in range(N):
    n = arr[i]
    idx = 0
    mx = 0
    for j in range(n):
        if table[j] > mx:
            mx = table[j]
            idx = j
    table[n] = mx + 1
    route[n] = route[idx] + f' {n}'

result = 0
mx_idx = 0
for i in range(1, 1001):
    if table[i] > result:
        result = table[i]
        mx_idx = i
print(result)
print(route[mx_idx][2:])