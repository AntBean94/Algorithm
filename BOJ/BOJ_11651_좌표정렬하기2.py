# BOJ 11651 좌표 정렬하기 2

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    x, y = map(int, input().split())
    arr.append([y, x])
arr.sort()
for y, x in arr:
    sys.stdout.writelines(f'{x} {y}\n')