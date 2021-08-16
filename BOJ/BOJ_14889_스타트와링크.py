# BOJ 14889 스타트와 링크 

# 브루트포스 풀이

import itertools
import sys
input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

member = set(i for i in range(1, N + 1))
min_dif = 1000000000
# 팀 뽑기
comb = list(itertools.combinations(member, N//2))
for t in range(len(comb)//2):
    a_team = set(comb[t])
    b_team = set(member) - a_team
    a_point = 0
    b_point = 0
    for s in a_team:
        for t in a_team:
            a_point += info[s-1][t-1]
    for s in b_team:
        for t in b_team:
            b_point += info[s-1][t-1]
    if abs(a_point - b_point) < min_dif:
        min_dif = abs(a_point - b_point)
print(min_dif)