# BOJ 1932 정수 삼각형

'''

1
1 2
1 2 3
1 2 3 4

1 to 1, 2
2 to 2, 3
3 to 3, 4

높이: 0, 1, 2, 3, 4, ...N-1
가로: 


'''

import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

table = [[0] * i for i in range(N + 1)]
table[1][0] = cost[0][0]

for i in range(N):
    for j in range(i):
        for k in range(2):
            if not table[i + 1][j + k]:
                table[i + 1][j + k] = table[i][j] + cost[i][j + k]
            elif table[i][j] + cost[i][j + k] > table[i + 1][j + k]:
                table[i + 1][j + k] = table[i][j] + cost[i][j + k]
print(max(table[N]))