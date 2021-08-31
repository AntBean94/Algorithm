# BOJ 1920 수 찾기

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
sub = list(map(int, input().split()))
l, r = 0, len(arr) - 1

# 정렬
arr.sort()

def binary(arr, target, l, r):
    m = (l + r) // 2
    if arr[m] == target:
        print(1)
        return
    if l == r:
        print(0)
        return
    if target < arr[m]:
        binary(arr, target, l, m)
    else:
        binary(arr, target, m + 1, r)

# 이분탐색
for s in sub:
    binary(arr, s, l, r)
