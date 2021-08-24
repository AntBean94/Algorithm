# BOJ 11053 가장 긴 증가하는 부분 수열 (Longest Increasing Subsequence)

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
table = [0] * (1001)
table[arr[0]] = 1

for i in arr:
    for j in range(i):
        if table[j] + 1 > table[i]:
            table[i] = table[j] + 1
print(max(table))