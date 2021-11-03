# BOJ 15661 링크와 스타트

'''
접근 방법

ex) 
6명 팀
팀 A = 1, 2, 5
팀 B = 3, 4, 6

sum(A) = x
sum(B) = y
중립 = m 일 때,

y = total - x - m
y - x = total - 2x - m

즉 팀 A멤버의 행, 열의 총합을 구해두고
총합에서 빼면 중립값은 한번씩, 자신의 값은 두번씩 감소하므로
sum(B) - sum(A) = y - x 를 만족
이 값의 최솟값을 찾으면 된다.
'''

from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
member = [list(map(int, input().split())) for _ in range(N)]
# 멤버 부분합
P = [0] * N
total = sum([sum(m) for m in member])
for i in range(N):
    for j in range(N):
        P[i] += member[i][j]
        P[j] += member[i][j]

ans = 100000000
for i in range(2, N // 2 + 1):
    for team_a in combinations([j for j in range(N)], i):
        result = abs(total - sum(P[i] for i in team_a))
        if result < ans: ans = result
        if ans == 0:
            print(0)
            exit()
print(ans)