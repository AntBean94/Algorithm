# BOJ 1620 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
book = {}
for i in range(1, N + 1):
    monster = input().rstrip()
    book[str(i)] = monster
    book[monster] = i
for i in range(M):
    print(book[input().rstrip()])