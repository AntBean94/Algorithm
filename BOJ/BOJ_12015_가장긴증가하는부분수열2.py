# BOJ 12015 가장 긴 증가하는 부분 수열 2



import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

table = [0]

ans = 0
for i in arr:
    if i > table[-1]:
        table.append(i)
    else:
        table[bisect.bisect_left(table, i)] = i
print(len(table) - 1)