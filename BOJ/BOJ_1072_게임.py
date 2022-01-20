# BOJ 1072 게임

'''
if Z = 99면

Z = int(Y / X * 100)
Z' = (Y + K) / (X + K) * 100
Z' = Z + 1

(Z + 1)(X + K) / 100 = Y + K

ZX + ZK + X + K = 100Y + 100K
99K - ZK = ZX + X - 100Y
K = (ZX + X - 100Y) / (99 - Z)
K' = ceil(K)
'''

import math

X, Y = map(int, input().split())
Z = 100 * Y // X
D = 99 - Z

if D <= 0: print(-1)
else: print(math.ceil((Z * X + X - 100 * Y) / D))