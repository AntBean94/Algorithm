# BOJ 15661 링크와 스타트

'''
링크와 스타트

N 명
인원수는 같지 않아도 되지만 1명 이상
Sij Sji 모두 더해야 한다.
=> 애초에 두 점의 합으로 계산

능력치 차이를 최소화

완탐: 2 ^ 20 = 100만

4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

=>

4
0 5 9 6
0 0 6 10
0 0 0 7
0 0 0 0

1과 2가 팀이 되면

'''

from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
member = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N // 2 + 1):
    for team_a in combinations([j for j in range(N)], i):
        print(team_a, type(team_a))
