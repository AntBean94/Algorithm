# BOJ 11650 좌표 정렬하기

import sys
input = sys.stdin.readline

arr = []
N = int(input())
for i in range(N):
    arr.append(list(map(int, input().split())))
arr.sort()
for a in arr:
    sys.stdout.writelines(" ".join(map(str, a)) + '\n')