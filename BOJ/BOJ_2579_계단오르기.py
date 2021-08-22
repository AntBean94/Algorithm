# BOJ 2579 계단 오르기

'''
계단 오르기

계단을 세번 연속으로 오르는건 안됨

2차원 배열 활용?

[20, 0]
[0, 30]
[45, 0]
[45, 60]
[65, ]

1칸 점프는 인덱스 2번으로 이동
2칸 점프는 인덱스 1번으로 이동

인덱스 1번은 1,2칸 점프 모두 가능하지만
인덱스 2번은 2칸 점프만 가능하다.

해당 위치로 이동 했을 때 값이 없거나 자기보다 작으면 바꿈

뒤에서 앞으로...

'''

import sys
input = sys.stdin.readline

N = int(input())
cost = [0] + [int(input()) for _ in range(N)]

table = [[0, 0] for _ in range(N + 1)]
table[N][0] = cost[N]

for i in range(N, 0, -1):
    for j in range(2):
        if not j:
            # 한칸 점프
            if table[i][j] + cost[i - 1] > table[i - 1][1]:
                table[i - 1][1] = table[i][j] + cost[i - 1]
            # 두칸 점프
            if i - 2 < 0: continue
            if table[i][j] + cost[i - 2] > table[i - 2][0]:
                table[i - 2][0] = table[i][j] + cost[i - 2]
        else:
            # 두칸 점프만 가능
            if i - 2 < 0: continue
            if table[i][j] + cost[i - 2] > table[i - 2][0]:
                table[i - 2][0] = table[i][j] + cost[i - 2]
ans = 0
for i in range(2):
    for j in range(2):
        if table[i][j] > ans:
            ans = table[i][j]
print(ans)