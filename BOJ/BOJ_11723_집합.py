# BOJ 11723 집합

'''
비트마스크

시프트
1 << 2
001 => 100

추가(or)
00000
00100
00100

삭제(~and)
00100
11011
00000
'''

import sys
input = sys.stdin.readline
N = int(input())
S = 0
for i in range(N):
    cmd = list(input().split())
    if len(cmd) == 2: n = int(cmd[1]) - 1
    cmd = cmd[0]
    if cmd == "add": S = S | 1 << n
    elif cmd == "remove": S = S & ~(1 << n)
    elif cmd == "check":
        if S & 1 << n: print(1)
        else: print(0)
    elif cmd == "toggle":
        if S & 1 << n: S = S & ~(1 << n)
        else: S = S | 1 << n
    elif cmd == "all": S = 2 ** 20 - 1
    else: S = 0