# BOJ 1208 부분수열의 합 2

'''
크기가 양수인 부분수열의 합
'''

import bisect
from itertools import combinations as cb
N, S = map(int, input().split())
arr = list(map(int, input().split()))

m = N // 2
arr_a = []
arr_b = []
# 절반으로 분할
for i in range(m + 1):
    for case in cb(arr[:m], i):
        arr_a.append(sum(case))
for i in range(N - m + 1):
    for case in cb(arr[m:], i):
        arr_b.append(sum(case))
t = len(arr_b)
arr_b.sort()
ans = 0
check = {}
for b in arr_b:
    if b in check: check[b] += 1
    else: check[b] = 1
for a in arr_a:
    i = bisect.bisect_left(arr_b, S - a)
    if i >= t: continue
    if arr_b[i] + a == S:
        ans += check[arr_b[i]]
if S == 0: print(ans - 1)
else: print(ans)