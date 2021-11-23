# BOJ 17219 비밀번호 찾기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = {}
for i in range(N):
    domain, pwd = input().split()
    table[domain] = pwd
for i in range(M):
    print(table[input().rstrip()])