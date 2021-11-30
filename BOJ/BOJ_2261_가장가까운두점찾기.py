# BOJ 2261 가장 가까운 두 점 찾기

'''


'''

import bisect
import sys
input = sys.stdin.readline

def dist(p1, p2):
    result = p1[0]

def change(arr):
    return set(arr[1], arr[0])

N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()

candidate = set([change(arr[0]), change(arr[1])])
ans = dist(arr[0], arr[1])
start = 0
for i in range(1, N):
    continue
