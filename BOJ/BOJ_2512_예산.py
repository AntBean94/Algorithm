# BOJ 2512 예산

'''
정수 상한액을 계산해보자.

예산안은 최대 10,000개

총예산의 범위는 2^30

상한선 선정과 상한선에 포함되는 금액을 찾을 때 이분탐색 활용
'''

import bisect

N = int(input())
req = sorted(list(map(int, input().split())))
total = int(input())
ans = 0

# 1. 상한액 탐색
l, r = 0, 100000
while l <= r:
    m = int((l + r) / 2)
    a = bisect.bisect_left(req, m)
    tmp = sum(req[:a]) + m * (N - a)
    if a == N and tmp <= total: ans = req[-1]; break
    if tmp > total: r = m - 1
    else: l = m + 1; ans = m
print(ans)