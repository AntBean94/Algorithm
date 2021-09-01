# BOJ 2805 나무 자르기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
tree = {}
for a in arr:
    if a in tree:
        tree[a] += 1
    else:
        tree[a] = 1

def check(k):
    result = 0
    for height, cnt in tree.items():
        if height <= k: continue
        tmp = (height - k) * cnt
        result += tmp
    return result

def binary(s, e):
    if s == e:
        print(s - 1)
        return
    m = (s + e) // 2
    if check(m) >= M:
        return binary(m + 1, e)
    else:
        return binary(s, m)

binary(0, 2000000001)