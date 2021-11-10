# BOJ 1764 듣보잡

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
listen = set([input().rstrip() for _ in range(N)])
see = set([input().rstrip() for _ in range(M)])
result = sorted(listen & see)
print(len(result))
for i in result:
    print(i)