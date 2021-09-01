# BOJ 11722 가장 긴 감소하는 부분 수열

import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

table = [0]
for i in arr[::-1]:
    if i > table[-1]:
        table.append(i)
    else:
        table[bisect.bisect_left(table, i)] = i

print(len(table) - 1)