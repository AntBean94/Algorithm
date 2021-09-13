# BOJ 18870 좌표 압축

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dic = {}
for a in arr:
    if a in dic: dic[a] += 1
    else: dic[a] = 1

cnt = 0
seq = sorted(dic)
new_dict = {}
for s in seq:
    new_dict[s] = cnt
    cnt += 1
for a in arr:
    print(new_dict[a], end=" ")