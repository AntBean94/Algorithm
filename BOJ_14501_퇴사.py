# BOJ 14501 퇴사

# 완전 탐색

import sys
import itertools
input = sys.stdin.readline
N = int(input())
plan = [[0, 0]] + [list(map(int, input().split())) for i in range(N)]
max_benefit = 0
for i in range(1, N+1):
    for case in itertools.combinations([i for i in range(1, N+1)], i):
        benefit = 0
        time = 0
        pre_day = 0
        for day in case:
            if day < pre_day + time:
                break
            if day + plan[day][0] > N + 1:
                break
            benefit += plan[day][1]
            pre_day = day
            time = plan[day][0]
        if benefit > max_benefit:
            max_benefit = benefit
print(max_benefit)    