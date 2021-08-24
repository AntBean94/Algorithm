# BOJ 2156 포도주 시식

'''

6 10 13 9 8 1

4 5 1 1 1 3 10
4 5 1 1 3 1 10

[0, 6, 6]
[6, 10, 16]
[16, 19, 23]
[23, 25, 28]
[28, 31, 33]
[33, 29, 32]

0: 0, 1
1: 0, 2
2: 0

'''

idx = [[0, 1], [0, 2], [0]]

import sys
input = sys.stdin.readline

N = int(input())
table = [[0] * 3 for _ in range(N + 1)]
wine = [int(input()) for _ in range(N)]

for i in range(N):
    for j in range(3):
        for d in idx[j]:
            if d:
                if table[i][j] + wine[i] > table[i + 1][d]:
                    table[i + 1][d] = table[i][j] + wine[i]
            else:
                if table[i][j] > table[i + 1][d]:
                    table[i + 1][d] = table[i][j]
print(max(table[N]))

